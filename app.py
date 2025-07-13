import streamlit as st
from modules.qa_with_retriever import answer_query_with_gemini

# --- Page config ---
st.set_page_config(
    page_title="🇱🇰 Gov Services FAQ Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar ---
with st.sidebar:
    st.title("🤖 Sri Lanka Gov FAQ Bot")
    st.markdown("""
    Welcome!  
    Ask questions about **Sri Lankan government services** in **Tamil**, **Sinhala**, or **English**.  
    Get quick, accurate answers powered by AI.

    **✨ Technologies:**  
    - Google Gemini 1.5 Flash  
    - Cohere Multilingual Embeddings  
    - LangChain & ChromaDB  

    **How to use:**  
    Just type your question below and get instant replies!

    **Made by [Vithusan V](https://github.com/thasvithu)**  
    📧 [Contact Me](mailto:thasvithu@gmail.com)

    ---
    _Disclaimer: This bot provides informational answers and is not an official government service._
    """)
    st.caption("Powered with ❤️ by Gemini, Cohere & Streamlit")

# --- Main UI ---
st.markdown(
    "<h2 style='text-align:center; margin-bottom:0;'>🇱🇰 Government Services FAQ Assistant</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; color: gray; margin-top:5px;'>Ask questions in Tamil, Sinhala, or English</p>",
    unsafe_allow_html=True
)

# --- Session state for chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display chat messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# --- User input ---
query = st.chat_input("Type your question about passports, NIC, land docs, and more...")
if query:
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})

    # Display user message
    with st.chat_message("user"):
        st.markdown(query)

    # Bot response with spinner
    with st.chat_message("assistant"):
        with st.spinner("Getting answer..."):
            result = answer_query_with_gemini(query)

            # Parse response
            if isinstance(result, dict):
                answer = result.get("answer", "")
                sources = result.get("sources", [])
            else:
                answer = result
                sources = []

            # Format answer with line breaks for readability
            formatted_answer = answer.replace("\n", "<br>")

            st.markdown(formatted_answer, unsafe_allow_html=True)

            # Show sources if any
            if sources:
                st.markdown("<hr>", unsafe_allow_html=True)
                st.markdown("**Sources:**")
                for s in sources:
                    st.markdown(f"- `{s}`")

    # Append assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": formatted_answer})
