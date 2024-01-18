#221RDB511 Artūrs Brūvers DS-11 2. Kurss
import os
import time
from PyPDF2 import PdfMerger

def merge_pdfs(input_folder, output_file):
    merger = PdfMerger()

    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

    pdf_files.sort()

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        merger.append(pdf_path)

    merger.write(output_file)
    merger.close()

if __name__ == "__main__":
    input_folder = "PDFs"

    output_file_name = input("Ievadiet PDF faila Nosaukumu bez formāta noteikšanas: ")
    output_file = f"{output_file_name}.pdf"

    start_time = time.time()

    merge_pdfs(input_folder, output_file)

    end_time = time.time()
    elapsed_time = end_time - start_time

    file_size = os.path.getsize(output_file)

    if file_size < 1024:
        size_str = f"{file_size} bytes"
    elif file_size < 1024 ** 2:
        size_str = f"{file_size / 1024:.2f} KB"
    else:
        size_str = f"{file_size / (1024 ** 2):.2f} MB"

    print(f"Jūsu PDF fails ir gatavs ({output_file})")
    print(f"Izpildes laiks: {elapsed_time:.2f} sekundes")
    print(f"PDF faila izmērs: {size_str}")
