#221RDB511 Artūrs Brūvers 
import os
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

    output_file = "merged_output.pdf"

    merge_pdfs(input_folder, output_file)
