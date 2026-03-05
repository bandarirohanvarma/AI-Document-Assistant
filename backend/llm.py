import streamlit as st
from groq import Groq

# Initialize Groq client using Streamlit secrets
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_answer(context, question):

    prompt = f"""
You are an AI assistant that answers questions using the provided document context.

If the answer is not present in the context, say:
"I could not find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content