import streamlit as st
import os

from utils.pdf_loader import load_pdf
from utils.chunking import split_text
from backend.vector_store import create_vector_store
from backend.rag_pipeline import ask_question

# Create required folders if they don't exist
os.makedirs("data", exist_ok=True)
os.makedirs("chroma_db", exist_ok=True)

st.title("📄 AI Document Assistant")

st.write("Upload a PDF and ask questions about the document.")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:

    # Save uploaded file
    file_path = os.path.join("data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Document uploaded successfully!")

    # Process document
    with st.spinner("Processing document..."):

        text = load_pdf(file_path)

        chunks = split_text(text)

        create_vector_store(chunks)

    st.success("Document processed and stored in vector database!")

# Ask question
question = st.text_input("Ask a question about the document")

if question:

    with st.spinner("Thinking..."):

        answer = ask_question(question)

    st.write("### Answer")
    st.write(answer)