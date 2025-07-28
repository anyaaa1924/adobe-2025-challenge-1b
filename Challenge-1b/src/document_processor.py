import os
import fitz  # PyMuPDF

def extract_sections_from_pdfs(folder_path):
    sections = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder_path, filename)
            doc = fitz.open(filepath)
            for page_num, page in enumerate(doc):
                text = page.get_text().strip()
                if not text:
                    continue
                sections.append({
                    "document": filename,
                    "page": page_num + 1,
                    "title": text[:50].replace("\n", " "),  # First few words as title
                    "text": text
                })
    return sections
