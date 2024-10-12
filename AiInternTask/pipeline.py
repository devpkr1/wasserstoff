import os
import time
import pymongo
from pymongo import MongoClient
import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
import concurrent.futures

# Download necessary NLTK resources (run this once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')  # Adjust if your MongoDB has different settings
db = client['pdf_summary_database']  # Create or access the database
collection = db['pdf_documents']  # Create or access the collection

def get_pdf_files_from_folder(folder_path):
    """Fetch all PDF files from the specified folder."""
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    return pdf_files

def count_pdf_pages(file_path):
    """Return the number of pages in the PDF."""
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        return len(reader.pages)

def categorize_pdf(file_path):
    """Categorize PDF as short, medium, or long based on page count."""
    page_count = count_pdf_pages(file_path)
    if page_count <= 10:
        return "short"
    elif page_count <= 30:
        return "medium"
    else:
        return "long"

def extract_text_from_pdf(file_path):
    """Extract text from the PDF."""
    text = ''
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def store_pdf_metadata_in_mongodb(pdf_file, folder_path, category):
    """Stores the initial metadata of the PDF in MongoDB."""
    file_path = os.path.join(folder_path, pdf_file)
    file_size = os.path.getsize(file_path)

    # Create a metadata dictionary
    metadata = {
        'file_name': pdf_file,
        'file_path': file_path,
        'file_size': file_size,
        'category': category,
        'summary': None,  # Will be updated after summarization
        'keywords': None  # Will be updated after keyword extraction
    }

    # Insert the metadata into MongoDB
    collection.insert_one(metadata)
    print(f"Inserted metadata for {pdf_file} into MongoDB")

def update_pdf_summary_and_keywords(pdf_file, summary, keywords):
    """Update MongoDB entry with the summary and keywords."""
    collection.update_one(
        {'file_name': pdf_file},
        {'$set': {'summary': summary, 'keywords': keywords}}
    )
    print(f"Updated summary and keywords for {pdf_file} in MongoDB")

def summarize_text_based_on_length(text, category):
    """Summarize text based on document length category (short, medium, long)."""
    sentences = sent_tokenize(text)

    if category == "short":
        num_sentences = 2  # Concise summary for short documents
    elif category == "medium":
        num_sentences = 4  # Medium-length summary for medium documents
    elif category == "long":
        num_sentences = 7  # Detailed summary for long documents
    else:
        num_sentences = 3  # Default to 3 sentences if category is undefined

    if len(sentences) <= num_sentences:
        return text  # Return the full text if it has fewer sentences than needed

    words = nltk.word_tokenize(text.lower())
    word_frequencies = Counter(words)

    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]

    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(ranked_sentences[:num_sentences])

    return summary

def extract_keywords(text, num_keywords=5):
    """Extracts the top keywords from the text."""
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text.lower())
    
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
    
    word_frequencies = Counter(filtered_words)
    
    keywords = [word for word, freq in word_frequencies.most_common(num_keywords)]
    return keywords

def process_single_pdf(pdf_file, folder_path):
    """Process a single PDF file."""
    start_time = time.time()  # Start timer for individual PDF

    try:
        file_path = os.path.join(folder_path, pdf_file)
        category = categorize_pdf(file_path)
        print(f"Processing {pdf_file}: {category} document")

        # Extract text from the PDF
        text = extract_text_from_pdf(file_path)

        # Summarize the text based on document length
        summary = summarize_text_based_on_length(text, category)

        # Extract keywords from the text
        keywords = extract_keywords(text)

        # Store metadata in MongoDB before processing
        store_pdf_metadata_in_mongodb(pdf_file, folder_path, category)

        # Update MongoDB with the summary and keywords
        update_pdf_summary_and_keywords(pdf_file, summary, keywords)

    except Exception as e:
        print(f"Error processing {pdf_file}: {str(e)}")
    finally:
        end_time = time.time()  # End timer
        print(f"Finished processing {pdf_file} in {end_time - start_time:.2f} seconds.")

def process_pdfs_concurrently(folder_path):
    """Process PDFs concurrently and measure performance."""
    pdf_files = get_pdf_files_from_folder(folder_path)

    start_time = time.time()  # Start timer for overall processing
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda pdf: process_single_pdf(pdf, folder_path), pdf_files)
    end_time = time.time()  # End timer

    print(f"Processed {len(pdf_files)} PDFs in {end_time - start_time:.2f} seconds.")

# Test Code
if __name__ == "__main__":
    folder_path = r"C:\Users\Pradeep Kumar\Desktop\PDF Documents"  # folder path
    process_pdfs_concurrently(folder_path)
