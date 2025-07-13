import os
import google.generativeai as genai
from dotenv import load_dotenv
from modules.retriever import get_retriever

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

retriever = get_retriever(
    persist_directory="./chroma_store",
    model_name="embed-multilingual-v3.0"
)

def answer_query_with_gemini(query: str) -> str:
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant documents found."

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""You are a multilingual assistant. Answer the question in the same language it is asked.
    
    Context:
    {context}

    Question:
    {query}
    """
    try:
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API error: {e}"
