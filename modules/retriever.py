from langchain_chroma import Chroma
from langchain_community.embeddings import CohereEmbeddings

import os

def get_retriever(persist_directory="./chroma_store", model_name="embed-multilingual-v3.0"):
    embedding = CohereEmbeddings(
        cohere_api_key=os.getenv("COHERE_API_KEY"),
        model=model_name,
        user_agent="langchain"
    )

    vectorstore = Chroma(   
        persist_directory=persist_directory,
        embedding_function=embedding
        
    )
    
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
