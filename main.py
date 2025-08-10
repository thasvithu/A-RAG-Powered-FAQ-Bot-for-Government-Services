from modules.pdf_loader import load_pdf
from modules.text_splitter import split_text
from modules.embed_store import embed_and_store_documents
from modules.qa_with_retriever import answer_query_with_gemini
import hashlib
import json
import os

PROCESSED_RECORD_FILE = "processed_pdfs.json"

def get_file_hash(file_path):
    """Generate a hash for the file content."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def load_processed_records():
    if os.path.exists(PROCESSED_RECORD_FILE):
        with open(PROCESSED_RECORD_FILE, "r") as f:
            return json.load(f)  # now returns a dict {filename: hash}
    return {}

def save_processed_records(processed_dict):
    with open(PROCESSED_RECORD_FILE, "w") as f:
        json.dump(processed_dict, f, indent=4)

def process_pdf(pdf_path):
    processed = load_processed_records()
    pdf_hash = get_file_hash(pdf_path)

    # Check if this file was already processed with the same hash
    if pdf_path in processed and processed[pdf_path] == pdf_hash:
        print("PDF already processed, skipping.")
        return

    pdf_text = load_pdf(pdf_path)
    chunks = split_text(pdf_text, chunk_size=1000, chunk_overlap=100)
    vectorstore = embed_and_store_documents(
        chunks, persist_directory="./chroma_store", model_name="embed-multilingual-v3.0"
    )

    # Save or update the hash for this file path
    processed[pdf_path] = pdf_hash
    save_processed_records(processed)
    print("PDF processed and embeddings stored successfully.")

# Example usage
process_pdf("./data/Passport1.pdf")
