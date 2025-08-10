<div align="center">

# 🇱🇰 RAG‑Powered Government Services FAQ Bot

Multilingual (Sinhala | Tamil | English) Retrieval‑Augmented Generation chatbot that answers citizen questions about Sri Lankan government services using official PDF documents.

</div>

---

## 🚀 Overview
This project implements a Retrieval‑Augmented Generation (RAG) pipeline: it ingests official PDFs, chunks & embeds them with Cohere multilingual embeddings, stores vectors in ChromaDB, retrieves the most relevant passages for a user question, and uses Google Gemini to generate grounded, bullet‑point answers in the same language as the query.

## ✨ Key Features
- Multilingual query + answer (Sinhala / Tamil / English) — responds in the query language
- Grounded answers: refuses to hallucinate outside provided context
- Persistent vector store (Chroma) — fast restarts without re‑embedding
- Streamlit chat UI with history
- Modular pipeline (loader → splitter → embed/store → retriever → LLM)

## 🧱 Tech Stack
- LangChain (documents, splitting, orchestration)
- Cohere Multilingual Embeddings (`embed-multilingual-v3.0`)
- ChromaDB (vector storage)
- Google Gemini 1.5 Flash (generation)
- Streamlit (UI)
- PyPDF (`pypdf` via `PyPDFLoader`)

## 📂 Project Structure
```
app.py                     # Streamlit chat application
main.py                    # Simple ingestion + demo query script
modules/
	pdf_loader.py           # PDF -> Documents
	text_splitter.py        # Recursive chunking
	embed_store.py          # Embedding + persistence
	retriever.py            # Retriever factory
	qa_with_retriever.py    # Retrieval + Gemini answer
data/                     # Source PDFs (ingestion corpus)
chroma_store/             # Persisted Chroma vector DB
notebooks/                # Experiments & workflow exploration
requirements.txt          # Python dependencies (pin / install)
```

## 🔐 Environment Variables
Create a `.env` file in the project root:
```
COHERE_API_KEY=your_cohere_key
GOOGLE_API_KEY=your_gemini_key
```

## 🛠️ Setup
```powershell
# (Optional) Create & activate virtual environment
python -m venv .venv
./.venv/Scripts/Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## 📥 Ingest Documents
Place PDF files in `data/` then run:
```powershell
python main.py
```
This will:
1. Load the sample `Passport1.pdf`
2. Split into chunks
3. Embed & persist to `./chroma_store`
4. Run a sample question

Re‑run only when adding or updating source PDFs. (A future improvement could add duplicate chunk detection.)

## 💬 Run the Chat App
```powershell
streamlit run app.py
```
Open the provided local URL. Ask questions such as:
- Sinhala: ශ්‍රී ලංකාවේ පැස්පෝට් ලබාගැනීමේ ක්‍රියාවලිය මොකක්ද?
- Tamil: இலங்கையில் பாஸ்போர்ட் பெற எந்த படிகள்?
- English: What documents are needed for a Sri Lankan passport?

## ⚙️ Configuration (current defaults)
| Aspect | Location | Default | Notes |
|--------|----------|---------|-------|
| Chunk size | `text_splitter.py` | 512 | Increase for fewer, larger chunks |
| Chunk overlap | `text_splitter.py` | 64 | Maintain semantic continuity |
| Embedding model | `embed_store.py` / `retriever.py` | embed-multilingual-v3.0 | Cohere multilingual |
| Retriever k | `retriever.py` | 5 | Number of context chunks sent to Gemini |
| Vector store dir | Code args | ./chroma_store | Persist across sessions |

To adjust, edit the corresponding module or refactor into a config file (see Roadmap).

## 🧪 Testing Ideas (Not Yet Implemented)
Planned lightweight checks:
- Ingestion smoke test: ensure ≥1 chunk, embeddings count matches
- Retrieval test: known query returns at least one relevant chunk
- Prompt safety test: injection attempt returns refusal phrase

## 🔄 RAG Flow
1. Load PDFs → LangChain Documents (page metadata)
2. Split into overlapping chunks (recursive splitter)
3. Embed chunks (Cohere) → store vectors (Chroma persistent)
4. User asks a question → retrieve top-k similar chunks
5. Construct grounded multilingual prompt → Gemini Flash
6. Return bullet‑point answer (no hallucinated extras)

## 🗺️ Roadmap / Next Steps
- [ ] Add metadata (page, source) to answers as citations
- [ ] Structured response `{ answer, sources[] }` always
- [ ] Config file (YAML or `.env` expansions) for tunables
- [ ] Duplicate chunk hash + skip re‑embedding
- [ ] Reranker (Cohere Rerank or cross‑encoder) post‑retrieval
- [ ] Evaluation notebook (Recall@K, groundedness LLM judge)
- [ ] Streaming responses in UI
- [ ] Upload new PDF via UI + background embedding job
- [ ] Semantic cache for repeated queries
- [ ] Improved prompt injection mitigation

## ⚠️ Disclaimer
This assistant provides informational responses based on supplied documents and is **not** an official government service. Always verify critical requirements with official sources.

## 📄 License
See `LICENSE` for details.

## 🙌 Acknowledgements
- Cohere & Google for API access
- LangChain & Chroma communities

---

Feel free to open issues or PRs to improve ingestion, evaluation, or multilingual robustness.