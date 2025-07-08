from modules.pdf_loader import load_pdf
from modules.text_splitter import split_text
from modules.embed_store import embed_documents

pdf_text = load_pdf("./data/Passport1.pdf")

print(pdf_text)


print ("\n --------------------------------------\n")

print("Splitting text into chunks...")
chunks = split_text(pdf_text, chunk_size=1000, chunk_overlap=100)
print(f"Number of chunks created: {len(chunks)}")

print ("\n --------------------------------------\n")

print("Embedding the chunks...")
embeddings = embed_documents(chunks, model_name="all-MiniLM-L6-v2")
print(f"Number of embeddings created: {len(embeddings)}")   
