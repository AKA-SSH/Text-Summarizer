from pdfminer.high_level import extract_text

def extract_text_from_pdf(filepath):
    text = extract_text(filepath)
    
    return text
