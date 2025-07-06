from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document

def split_text(documents: List[Document], chunk_size=1000, chunk_overlap=100):
    """
    Split a list of LangChain Document objects into smaller chunks.

    Args:
        documents (List[Document]): The documents to split.
        chunk_size (int): Max size of each chunk.
        chunk_overlap (int): Overlap between chunks.

    Returns:
        List[Document]: Smaller chunks with metadata preserved.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(documents) 
    return chunks
