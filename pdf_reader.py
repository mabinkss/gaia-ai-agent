
from pypdf import PdfReader

def extract_pdf_text(file_path: str) -> str:
    reader = PdfReader(file_path)
    pages = []

    for number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text:
            pages.append(f"Page {number}:\n{text}")

    if not pages:
        return "Aucun texte lisible dans ce PDF."

    return "\n\n".join(pages)
