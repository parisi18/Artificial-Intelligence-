import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY não foi definida. Crie um arquivo .env na raiz do projeto."
    )

client = Groq(api_key=api_key)

def ask_llm(messages):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content