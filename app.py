import streamlit as st
from modules.qa_with_retriever import answer_query_with_gemini

# Page config
st.set_page_config(page_title="Gov Services FAQ Bot", page_icon="🤖", layout="wide")

# Custom CSS for chat bubbles & styling
st.markdown(
    """
    <style>
    .chat-container {
        max-width: 700px;
        margin: 20px auto;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .chat-bubble {
        padding: 12px 20px;
        margin-bottom: 12px;
        border-radius: 20px;
        max-width: 80%;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        line-height: 1.4;
        font-size: 16px;
    }
    .user {
        background: #0b5ed7;
        color: white;
        margin-left: auto;
        text-align: right;
        border-bottom-right-radius: 0;
    }
    .bot {
        background: #e1e8f9;
        color: #202020;
        margin-right: auto;
        border-bottom-left-radius: 0;
    }
    .source-expander summary {
        font-weight: bold;
        cursor: pointer;
        font-size: 14px;
        margin-bottom: 8px;
        color: #0b5ed7;
    }
    .source-expander {
        font-size: 14px;
        color: #555;
        margin-top: 6px;
        margin-left: 10px;
    }
    .send-btn {
        background-color: #0b5ed7;
        color: white;
        border: none;
        padding: 10px 25px;
        border-radius: 8px;
        cursor: pointer;
        font-weight: 600;
        font-size: 16px;
        margin-left: 10px;
        transition: background-color 0.3s ease;
    }
    .send-btn:hover {
        background-color: #084298;
    }
    .input-area {
        display: flex;
        max-width: 700px;
        margin: 10px auto 30px;
    }
    textarea {
        flex-grow: 1;
        resize: vertical;
        padding: 12px 16px;
        font-size: 16px;
        border-radius: 12px;
        border: 1px solid #ccc;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        min-height: 60px;
        max-height: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🤖 Government Services FAQ Bot")
st.markdown("Ask your questions about government services, and get answers powered by Gemini AI.")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
def render_chat():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        # User query bubble
        st.markdown(f'<div class="chat-bubble user">{chat["query"]}</div>', unsafe_allow_html=True)
        
        # Bot answer bubble with replaced newlines
        answer_html = chat["answer"].replace("\n", "<br>")
        st.markdown(f'<div class="chat-bubble bot">{answer_html}</div>', unsafe_allow_html=True)

        # Sources collapsible
        if chat.get("sources"):
            source_html = '<details class="source-expander"><summary>Sources</summary><ul>'
            for src in chat["sources"]:
                source_html += f"<li>{src}</li>"
            source_html += "</ul></details>"
            st.markdown(source_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# Input form for query
with st.form(key="query_form", clear_on_submit=True):
    query = st.text_area("Your question", placeholder="E.g., How to apply for a passport in Sri Lanka?", label_visibility="collapsed")
    submit_btn = st.form_submit_button("Send")

if submit_btn and query.strip():
    with st.spinner("Thinking..."):
        # Call your backend function to get answer + sources
        response_text = answer_query_with_gemini(query)
        # Expecting response_text to be string or dict; adapt if needed
        answer = response_text if isinstance(response_text, str) else response_text.get("answer", "")
        sources = response_text.get("sources", []) if isinstance(response_text, dict) else []

        # Append to chat history
        st.session_state.chat_history.append({
            "query": query,
            "answer": answer,
            "sources": sources,
        })

# Render chat history
render_chat()
