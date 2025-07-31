# llm.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from prompt import create_prompts

load_dotenv()

def extract_invoice_fields(ocr_text: str) -> dict:
    messages, parser = create_prompts(ocr_text)

    llm = ChatGroq(
        temperature=0.1,
        model_name="llama3-8b-8192",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    response = llm.invoke(messages)
    return parser.parse(response.content).model_dump()  # Use .model_dump() if using Pydantic v2
