from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain.vectorstores import Chroma
from typing import List
import os

def embed_and_store_documents(
    documents: List[Document],
    persist_directory: str = "./chroma_store",
    model_name: str = "all-MiniLM-L6-v2"
):
    """
    Embed the list of documents using a pre-trained HuggingFace model
    and store the embeddings in a Chroma vector database.

    Args:
        documents (List[Document]): The documents to embed and store.
        persist_directory (str): Directory to persist the Chroma vector DB.
        model_name (str): The Hugging Face embedding model to use (default: "all-MiniLM-L6-v2").

    Returns:
        Chroma: The Chroma vector store instance with the stored embeddings.
    """
    # Initialize embedding model
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    
    # Create or load vectorstore and add documents with embeddings
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    
    # Persist to disk
    vectorstore.persist()

    print(f"Stored {len(documents)} documents with embeddings at {persist_directory}")
    
    return vectorstore
