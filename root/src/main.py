import os
from utils.text_extractor import extract_text_from_pdf
from utils.text_preprocessor import preprocess_text
from utils.text_chunking import semantic_chunking
from utils.text_summarization import abstractive_summary

import warnings
warnings.filterwarnings('ignore')

def main():
    # directory setup
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(base_dir)
    text_summarizer_dir = os.path.dirname(root_dir)
    pdf_dir = os.path.join(text_summarizer_dir, 'notebook', 'PDFs')
    
    # file path setup
    filename = '1.pdf'
    filepath = os.path.join(pdf_dir, filename)

    if not os.path.isfile(filepath):
        print(f'File not found: {filepath}')

    # main
    raw_text = extract_text_from_pdf(filepath)
    cleaned_text = preprocess_text(raw_text)
    clustered_text = semantic_chunking(cleaned_text)
    summary = abstractive_summary(clustered_text)

    print(summary)

if __name__ == '__main__':
    main()