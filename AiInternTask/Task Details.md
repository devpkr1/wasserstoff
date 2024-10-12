# **Internship Task: Domain-Specific PDF Summarization & Keyword Extraction Pipeline**
### **Objective**:

Design and implement a dynamic pipeline that processes multiple PDF documents from a desktop folder, generates **domain-specific** summaries and keywords, and stores them in a **MongoDB database**. The system must efficiently handle documents of varying lengths, from short to long, and update the database with summary and keyword data after each document is processed.
Your solution should prioritize concurrency, speed, and innovation.
---
## **Task Details**
### **1. PDF Ingestion & Parsing**
- **Requirement**: The pipeline should be able to process multiple PDFs from a folder on the desktop. It must handle documents of **varying lengths**:
    - Short PDFs (1-2 pages)
    - Medium PDFs (10-12 pages)
    - Long PDFs (30+ pages)
  
- **Concurrency**: Ensure the system can process multiple documents in parallel, managing system resources efficiently. The pipeline must handle large files and high volumes without crashing.
### **2. MongoDB Dataset Storage & JSON Updates**
- **Initial Storage**: When each PDF is ingested, its metadata (document name, path, size, etc.) must be stored in a MongoDB collection.
- **Post-Processing Update**: After summarization and keyword extraction, the MongoDB entry for each document must be updated with the JSON output, including the generated summary and extracted keywords.
### **3. Summarization & Keyword Extraction**
- **Summarization**: Dynamically generate summaries that are relevant to the domain you have chosen. The summary length and detail should correspond to the document length (e.g., a detailed summary for long documents, concise summaries for short ones).
- **Keyword Extraction**: Extract **non-generic**, domain-specific keywords that reflect key ideas or themes of the document. Avoid common or irrelevant keywords.
### **4. JSON Structure & MongoDB Updates**
- **JSON Format**: Summaries and keywords must be formatted in JSON, which will then be stored in the MongoDB document. Make sure to handle updates efficiently after processing each document.
- **Error Handling**: Log any errors (e.g., for corrupted PDFs or unsupported formats) and ensure that MongoDB records are not affected by such issues.
### **5. Concurrency & Performance**
- **Concurrency**: The pipeline should be designed to handle multiple documents simultaneously, leveraging parallel processing to improve speed.
- **Performance**: Provide data on how well the system scales, especially in terms of how quickly it processes large and multiple PDFs concurrently.
---
## **Additional Requirements**
- **Document Variety**: The pipeline must handle PDFs of varying lengths. Provide examples of short (1-2 pages), medium (10-12 pages), and long (30+ pages) documents in your testing.
- **Framework Restrictions**: The use of pre-built libraries or frameworks (such as Langchain or others) is permitted, but doing so will result in a deduction of up to **15 points**. Custom solutions will receive higher marks.
- **Testing & Performance**: You are expected to provide test results, especially regarding performance metrics such as concurrency, memory usage, and processing speed.
- **Error Handling**: Handle all edge cases, such as corrupted or encrypted PDFs, without interrupting the pipeline. All errors should be logged and MongoDB records updated accordingly.
