# 🧾 Invoice Field Extractor using EasyOCR + LLM

This project provides a scalable pipeline to extract structured fields from invoice images using **EasyOCR** for text extraction and **LLMs via LangChain** for field parsing.

---

## 🚀 Features

- **Supported Input Formats:** PDF, PNG, JPG (PDFs auto-converted to images)
- **OCR Engine:** EasyOCR
- **LLM Integration:** LangChain + Groq (Mixtral 8x7B)
- **Fields Extracted:**
  - Invoice Number
  - Invoice Date
  - Line Items (description, quantity, unit price, amount)
- **Scalable:** Easily extendable to extract any custom key-value fields by updating:
  - Prompts (`prompt.py`)
  - Output schema (`Pydantic` model in `llm.py`)
  - Optionally: fine-tune later for better performance

---

## 🧠 Tech Stack

| Component     | Technology        |
|---------------|------------------|
| Frontend      | Streamlit        |
| OCR           | EasyOCR          |
| LLM           | Mixtral 8x7B via LangChain-Groq |
| Schema Parsing| Pydantic + LangChain OutputParser |

---

## 🗂️ Folder Structure

Invoice_Extractor/
│
├── extractor/
│ ├── dataset/ # (Optional) Dataset samples
│ ├── app.py # Main Streamlit App
│ ├── easy_ocr.py # OCR logic using EasyOCR
│ ├── llm.py # LLM extraction logic
│ ├── prompt.py # Prompt template(s)
│ ├── .env # Environment variables
│
├── .env
├── .gitignore
├── README.md
├── pyproject.toml # Dependencies
├── uv.lock # Virtual environment lock file


## Create Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

## Install Dependencies

pip install -r requirements.txt

    Or if you're using uv:

uv pip install -r requirements.txt

## Setup Environment Variables

Create a .env file inside extractor/ and set the following:

GROQ_API_KEY=your_api_key_here

▶️ Run the App

cd extractor
streamlit run app.py