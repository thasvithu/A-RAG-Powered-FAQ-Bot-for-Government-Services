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
    # Step 1: Retrieve relevant context
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant documents found for your question."

    context = "\n\n".join(doc.page_content for doc in docs)

    # Step 2: Multilingual and bullet-point focused prompt
    prompt = f"""
    You are a trusted virtual assistant for Sri Lankan government services.

    Your job is to help users in **Tamil**, **Sinhala**, or **English**, depending on the language of the question. Do NOT translate. Reply in the same language.

    Use the following context from official documents to answer the user's question. 

    --- CONTEXT START ---
    {context}
    --- CONTEXT END ---

    --- USER QUESTION ---
    {query}
    --- END ---

    Guidelines:
    - ✅ Respond only using the given context.
    - ❌ If not found in context, say "I'm not sure based on the available information."
    - 🧾 Format the answer in **clear bullet points or numbered steps**.
    - 🔁 Do not repeat the question.

    Answer:
    """

    try:
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:  
        return f"Gemini API error: {e}"
