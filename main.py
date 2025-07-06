from modules.loaders.pdf_loader import load_pdf
from modules.chunkers.text_splitter import split_text

pdf_text = load_pdf("./data/Passport1.pdf")

print(pdf_text)


print ("\n --------------------------------------\n")

print("Splitting text into chunks...")
chunks = split_text(pdf_text, chunk_size=1000, chunk_overlap=100)
print(f"Number of chunks created: {len(chunks)}")