import streamlit as st
from modules.qa_with_retriever import answer_query_with_gemini

# Page Configuration
st.set_page_config(page_title="🇱🇰 Gov Services FAQ Bot", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🤖 FAQ Bot")
    st.markdown("""
    **About this App**

    Ask your questions in **Tamil**, **Sinhala**, or **English**  
    and get accurate answers about Sri Lankan Government services.

    ✨ **Tech Used**  
    - Gemini 1.5 Flash (Google)  
    - Cohere Multilingual Embeddings  
    - LangChain + ChromaDB

    **Built by [Vithusan.V](https://github.com/thasvithu)**  
    📧 [Contact Me](mailto:thasvithu@gmail.com)
    """)
    st.caption("Powered by ❤️ Gemini + Cohere + Streamlit")

# Main Title
st.markdown("<h2 style='text-align:center;'>🇱🇰 Government Services FAQ Bot</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Ask questions in Tamil | Sinhala | English</p>", unsafe_allow_html=True)

# Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# New User Query
query = st.chat_input("Ask about passport, NIC, land documents etc...")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Finding answer..."):
            response = answer_query_with_gemini(query)

            if isinstance(response, dict):
                answer = response.get("answer", "")
                sources = response.get("sources", [])
            else:
                answer = response
                sources = []

            formatted = answer.replace("\n", "<br>")
            st.markdown(formatted, unsafe_allow_html=True)

            if sources:
                st.markdown("**Sources:**")
                for s in sources:
                    st.markdown(f"- `{s}`")

    st.session_state.messages.append({"role": "assistant", "content": formatted})
