# prompt.py
from pydantic import BaseModel
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser

class InvoiceFields(BaseModel):
    invoice_number: str
    invoice_date: str
    line_items: list  # You can also define a custom LineItem model if needed

    class Config:
        from_attributes = True  # Required for StructuredOutputParser.from_orm()

def create_prompts(ocr_text: str):
    # 1. Define the parser
    parser = PydanticOutputParser(pydantic_object=InvoiceFields)

    # 2. Create the prompt template with format instructions
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an invoice extraction assistant."),
        ("user", "Extract invoice number, invoice date, and line items from the following text:\n\n{ocr_text}\n\n{format_instructions}")
    ])

    # 3. Format the final prompt with OCR text and parser instructions
    messages = prompt.format_messages(
        ocr_text=ocr_text,
        format_instructions=parser.get_format_instructions()
    )

    return messages, parser
