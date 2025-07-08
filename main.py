from modules.pdf_loader import load_pdf
from modules.text_splitter import split_text
from modules.embed_store import embed_and_store_documents
from modules.retriever import get_retriever
from modules.qa_with_retriever import qa_chain

"""

pdf_text = load_pdf("./data/Passport1.pdf")

print(pdf_text)


print ("\n --------------------------------------\n")

print("Splitting text into chunks...")
chunks = split_text(pdf_text, chunk_size=1000, chunk_overlap=100)
print(f"Number of chunks created: {len(chunks)}")

print ("\n --------------------------------------\n")

# Embedding and storing the documents
print("Embedding and storing documents...")
vectorstore = embed_and_store_documents(chunks, persist_directory="./chroma_store", model_name="all-MiniLM-L6-v2")
print("Documents embedded and stored successfully.")



retriever = get_retriever()
query = "How to apply for a passport in Sri Lanka?"
docs = retriever.get_relevant_documents(query)

for i, doc in enumerate(docs, 1):
    print(f"\nChunk {i}:\n{doc.page_content}")

"""

query = "How to apply for a passport in Sri Lanka?"

result = qa_chain.invoke({"query": query})

# You can now print both the result and sources
print("\nAnswer:")
print(result["result"])

print("\nSources:")
for doc in result["source_documents"]:
    print("-", doc.metadata.get("source", "No source info"))
