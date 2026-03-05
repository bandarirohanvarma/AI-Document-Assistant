from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(chunks):

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=embedding,
        persist_directory="chroma_db"
    )

    vectordb.persist()

    return vectordb