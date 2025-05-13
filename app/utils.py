import os
from PyPDF2 import PdfReader

def extract_text_from_pdfs(folder_path):
    all_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            with open(pdf_path, "rb") as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    all_text += page.extract_text() + "\n"
    return all_text.strip()
