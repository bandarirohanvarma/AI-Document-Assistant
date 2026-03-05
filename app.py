import streamlit as st
import os

from utils.pdf_loader import load_pdf
from utils.chunking import split_text
from backend.vector_store import create_vector_store
from backend.rag_pipeline import ask_question

st.title("📄 AI Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:

    file_path = os.path.join("data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    text = load_pdf(file_path)

    chunks = split_text(text)

    create_vector_store(chunks)

    st.success("Document processed successfully!")

question = st.text_input("Ask a question about the document")

if question:
    answer = ask_question(question)

    st.write("### Answer")
    st.write(answer)