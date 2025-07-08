from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEmbeddings
from langchain_chroma import Chroma
from transformers import pipeline

# 1. Setup embedding model (must be passed to Chroma)
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Load Chroma with the embedding function
persist_directory = "./chroma_store"
vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model  # THIS IS THE FIX
)
retriever = vectorstore.as_retriever()

# 3. Setup a light-weight language model (e.g., Flan-T5)
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=-1  # -1 for CPU
)

llm = HuggingFacePipeline(pipeline=pipe)

# 4. Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)
