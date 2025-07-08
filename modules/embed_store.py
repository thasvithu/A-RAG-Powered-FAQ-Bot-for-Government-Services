from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List

def embed_and_store_documents(
    documents: List[Document],
    persist_directory: str = "./chroma_store",
    model_name: str = "all-MiniLM-L6-v2"
):
    """
    Embed and store documents in Chroma vector store without overwriting existing data.
    """
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)

    # Load or create Chroma vectorstore
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )

    # Add new documents (append to existing)
    vectorstore.add_documents(documents)

    print(f"Stored {len(documents)} new documents at {persist_directory}")

    return vectorstore
