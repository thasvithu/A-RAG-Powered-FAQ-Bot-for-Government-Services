from langchain_chroma import Chroma
from langchain_community.embeddings import CohereEmbeddings
from langchain_core.documents import Document
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

def embed_and_store_documents(
    documents: List[Document],
    persist_directory: str = "./chroma_store",
    model_name: str = "embed-multilingual-v3.0"
):
    embedding_model = CohereEmbeddings(
        cohere_api_key=os.getenv("COHERE_API_KEY"),
        model=model_name,
        user_agent="langchain" # Optional user agent for tracking
    )

    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )

    vectorstore.add_documents(documents)
    print(f"✅ Stored {len(documents)} documents.")
    
    return vectorstore
