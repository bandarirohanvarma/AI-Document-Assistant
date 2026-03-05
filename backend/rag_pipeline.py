from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from backend.llm import generate_answer


def ask_question(question):

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding
    )

    docs = vectordb.similarity_search(question, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, question)

    return answer