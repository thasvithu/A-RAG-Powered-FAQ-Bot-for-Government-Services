from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List

def embed_documents(documents: List[Document], model_name: str = "all-MiniLM-L6-v2"):
    """
    Embed the list of documents using a pre-trained HuggingFace model.

    Args:
        documents (List[Document]): The documents to embed.
        model_name (str): The Hugging Face embedding model to use (default: "all-MiniLM-L6-v2").

    Returns:
        List[List[float]]: A list of embeddings (vector representation of the documents).
    """
    # Initialize embedding model
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    
    # Embed the documents
    embeddings = embedding_model.embed_documents([doc.page_content for doc in documents])

    return embeddings
