# PDF Summarization and Keyword Extraction Pipeline

## Overview
This project implements a pipeline for dynamically summarizing PDF documents and extracting relevant keywords based on their content. It supports handling multiple PDFs concurrently and stores the generated summaries and keywords in MongoDB.

## Features
- **PDF Ingestion**: Process multiple PDFs from a specified folder.
- **Summarization**: Generate dynamic summaries that adjust based on the document length (short, medium, long).
- **Keyword Extraction**: Extract meaningful, non-generic keywords from each document.
- **MongoDB Storage**: Store PDF metadata, summaries, and keywords in MongoDB.
- **Concurrency**: Process multiple PDFs concurrently using Python's `concurrent.futures` for faster performance.

## Explanation of the Solution

This project implements a **PDF Summarization and Keyword Extraction Pipeline** that processes PDF files, generates summaries, extracts keywords, and stores the results in a MongoDB database. The solution leverages concurrency to process multiple PDF files simultaneously, making it efficient even when dealing with a large number of documents.

### Key Components:

1. **PDF Ingestion**:
   - The pipeline starts by reading all PDF files from a specified folder.
   - The file paths and metadata (e.g., file size, document length) are stored in MongoDB.

2. **Dynamic Summarization**:
   - The pipeline categorizes each PDF document as **short**, **medium**, or **long** based on the number of pages.
   - A dynamic summarization method is used, where:
     - **Short documents** receive concise summaries (1-2 sentences).
     - **Medium documents** receive summaries of medium length (3-5 sentences).
     - **Long documents** get detailed summaries (5-7 sentences).
   - The summary generation process involves tokenizing the document’s text into sentences and ranking them based on the frequency of important words.

3. **Keyword Extraction**:
   - For each document, the most frequent and meaningful words are extracted as keywords.
   - Common stopwords (like "the," "and") are excluded to ensure that only significant keywords are included.
   - Keywords are extracted dynamically based on the content of each PDF.

4. **Concurrency**:
   - The pipeline uses Python's `concurrent.futures.ThreadPoolExecutor` to process multiple PDF files in parallel.
   - This enhances the performance of the solution, allowing it to handle large volumes of PDFs concurrently without significant delays.

5. **MongoDB Storage**:
   - Each PDF’s metadata, summary, and keywords are stored in MongoDB.
   - The structure of the data stored in MongoDB includes:
     - **File name**
     - **File path**
     - **File size**
     - **Document category** (short, medium, long)
     - **Summary** of the document
     - **Keywords** extracted from the document

### Solution Workflow:

1. **PDF Collection**: 
   - The pipeline scans a folder for PDFs and records basic metadata about each file.

2. **Text Extraction**: 
   - Text is extracted from each PDF using the `PyPDF2` library.

3. **Document Categorization**:
   - Based on the number of pages, the document is categorized as short, medium, or long.

4. **Summarization and Keyword Extraction**:
   - The pipeline summarizes the document and extracts keywords using the `nltk` library.
   - The length of the summary is adjusted according to the document category.

5. **Concurrency**:
   - Multiple documents are processed in parallel using threading, improving the overall processing time.

6. **MongoDB Integration**:
   - The extracted metadata, summaries, and keywords are stored in MongoDB in a well-structured format for future retrieval and analysis.

### Why This Solution?
- **Efficiency**: By using concurrency, the pipeline can process multiple PDF documents simultaneously, making it scalable and fast.
- **Dynamic Summarization**: The summarization process is flexible and adapts based on the document's length, ensuring that users get relevant and concise information.
- **Keyword Extraction**: Keywords provide a quick way to identify the core topics of a document, making the solution useful for summarizing large datasets.
- **Persistence with MongoDB**: Storing the results in MongoDB ensures that the information is easily accessible and can be further queried or analyzed.

## Performance Report

### Performance Metrics:
Here are the performance metrics observed during testing:

| Test Type                  | Processing Time | Memory Usage | CPU Usage |
|----------------------------|----------------|--------------|-----------|
| Single PDF Processing       | 2.80 seconds   | 145.02 MB    | 0.00 %    |
| Concurrent Processing (3 PDFs) | 5.55 seconds   | 146.43 MB    | 0.00 %    |

This report highlights the efficiency of the pipeline in terms of speed and resource utilization, showcasing how the application performs with single and multiple PDF files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-summarization-pipeline.git
    
 2. Navigate into the project folder:
    ```bash
    cd pdf-summarization-pipeline

3. Install required Python libraries:
    ```bash
    pip install -r requirements.txt

## Usage

1. Update the folder_path in the pipeline.py script to point to the folder containing your PDF files:
    ```bash
    folder_path = r"C:\\path\\to\\your\\pdf\\folder"

2. Run the pipeline:
   ```bash
   python pipeline.py

The script will process all PDF files in the specified folder, summarize them, extract keywords, and store the results in MongoDB.

## Dependencies

- Python 3.x
- PyPDF2
- nltk
- pymongo
- concurrent.futures (built into Python)

   To install dependencies, you can use:
    ```bash
    pip install -r requirements.txt

## MongoDB Setup
Make sure MongoDB is installed and running. You can use the default settings for MongoDB:

    mongodb://localhost:27017/


## Folder Structure
    .
    ├── pipeline.py         # Main Python script for processing PDFs
    ├── README.md           # Project documentation
    ├── requirements.txt    # Required Python packages
    └── pdf_folder/         # Folder containing your PDF files

## Example Output
### MongoDB Record:
Each PDF's metadata, summary, and keywords will be stored in a MongoDB collection in the following format:

```json
{
  "file_name": "example.pdf",
  "file_path": "/path/to/example.pdf",
  "file_size": 204800,
  "category": "medium",
  "summary": "This is a dynamically generated summary...",
  "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.


