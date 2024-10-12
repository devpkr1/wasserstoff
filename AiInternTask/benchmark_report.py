import timeit
import psutil
from concurrent.futures import ThreadPoolExecutor
from pipeline import process_single_pdf  # Adjust this import to match your module

# Define a folder path where PDFs are stored
UPLOAD_FOLDER = r"C:\Users\Pradeep Kumar\Desktop\PDF Documents"

def benchmark_single_pdf_processing(pdf_file):
    """Measure the time it takes to process a single PDF."""
    process = psutil.Process()  # Get the current process for monitoring
    start_time = timeit.default_timer()
    
    # Call process_single_pdf with both file and folder path
    process_single_pdf(pdf_file, UPLOAD_FOLDER)
    
    elapsed = timeit.default_timer() - start_time
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Memory usage in MB
    cpu_usage = process.cpu_percent(interval=1)  # Get CPU usage percentage
    
    return elapsed, memory_usage, cpu_usage

def benchmark_concurrent_processing(file_list):
    """Measure the time it takes to process multiple PDFs concurrently."""
    process = psutil.Process()  # Get the current process for monitoring
    start_time = timeit.default_timer()
    
    with ThreadPoolExecutor() as executor:
        # Provide both the file path and folder path
        executor.map(lambda pdf: process_single_pdf(pdf, UPLOAD_FOLDER), file_list)

    elapsed = timeit.default_timer() - start_time
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Memory usage in MB
    cpu_usage = process.cpu_percent(interval=1)  # Get CPU usage percentage
    
    return elapsed, memory_usage, cpu_usage

if __name__ == '__main__':
    # Define a list of PDF files for benchmarking
    file_list = [
        r"C:\Users\Pradeep Kumar\Desktop\PDF Documents\Circular Orders (Supplement).pdf",
        r"C:\Users\Pradeep Kumar\Desktop\PDF Documents\The Prevention of Money-laundering (Maintenance of Records) Rules, 2005.pdf",
        r"C:\Users\Pradeep Kumar\Desktop\PDF Documents\1292585113260.pdf"
    ]

    # Run the benchmarks
    single_pdf_time, single_memory, single_cpu = benchmark_single_pdf_processing(file_list[0])  # Process the first file
    concurrent_time, concurrent_memory, concurrent_cpu = benchmark_concurrent_processing(file_list)

    # Print the performance report
    print("### Performance Report ###")
    print(f"Single PDF processing time: {single_pdf_time:.2f} seconds")
    print(f"Single PDF memory usage: {single_memory:.2f} MB")
    print(f"Single PDF CPU usage: {single_cpu:.2f} %")
    print()
    print(f"Concurrent processing time (3 PDFs): {concurrent_time:.2f} seconds")
    print(f"Concurrent memory usage: {concurrent_memory:.2f} MB")
    print(f"Concurrent CPU usage: {concurrent_cpu:.2f} %")
