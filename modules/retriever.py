from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_retriever(persist_directory: str = "./chroma_store", model_name: str = "all-MiniLM-L6-v2"):
    """
    Load Chroma vector store and return a retriever for querying.

    Args:
        persist_directory (str): Path where the vector store is saved.
        model_name (str): Embedding model name used during storage.

    Returns:
        retriever: A retriever instance that can fetch relevant documents.
    """
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    # Load the existing Chroma vector store
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    # Create retriever from the vector store
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    return retriever
