# PDF Summarization and Keyword Extraction Pipeline

## Overview
This project implements a pipeline for dynamically summarizing PDF documents and extracting relevant keywords based on their content. It supports handling multiple PDFs concurrently and stores the generated summaries and keywords in MongoDB.

## Features
- **PDF Ingestion**: Process multiple PDFs from a specified folder.
- **Summarization**: Generate dynamic summaries that adjust based on the document length (short, medium, long).
- **Keyword Extraction**: Extract meaningful, non-generic keywords from each document.
- **MongoDB Storage**: Store PDF metadata, summaries, and keywords in MongoDB.
- **Concurrency**: Process multiple PDFs concurrently using Python's `concurrent.futures` for faster performance.

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


