import streamlit as st
import tempfile
import os
import pandas as pd
from easy_ocr import extract_text_easyocr  # Your OCR utility
from llm import extract_invoice_fields     # Your LLM parser

# Streamlit app configuration
st.set_page_config(page_title="Invoice Extractor", layout="centered")
st.title("📄 Invoice Field Extractor")
st.markdown("""
Upload an invoice image and extract the following:
- 📌 **Invoice Number**
- 🗓️ **Invoice Date**
- 📋 **Line Items**
""")

# Upload an invoice file
uploaded_file = st.file_uploader("Upload an invoice image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    # Show uploaded image (only for images, not PDF)
    if uploaded_file.type != "application/pdf":
        st.image(temp_path, caption="🖼 Uploaded Invoice", use_container_width=True)

    # Run OCR
    with st.spinner("🔍 Running OCR..."):
        try:
            ocr_text = extract_text_easyocr(temp_path)
        except Exception as e:
            st.error(f"❌ OCR failed: {e}")
            ocr_text = ""

    if ocr_text:
        st.text_area("📝 OCR Output", value=ocr_text, height=200)

        # Extract fields using LLM
        if st.button("🧠 Extract Fields with LLM"):
            with st.spinner("💡 Extracting invoice fields..."):
                try:
                    fields = extract_invoice_fields(ocr_text)
                except Exception as e:
                    st.error(f"❌ LLM extraction failed: {e}")
                    fields = {}

            if fields:
                st.success("✅ Extraction Complete")

                # Show invoice number & date
                st.subheader("📌 Extracted Fields")
                st.write(f"**Invoice Number:** `{fields.get('invoice_number', 'N/A')}`")
                st.write(f"**Invoice Date:** `{fields.get('invoice_date', 'N/A')}`")

                # Show line items
                st.subheader("🧾 Line Items")
                line_items = fields.get("line_items", [])
                if isinstance(line_items, list) and line_items:
                    try:
                        df = pd.DataFrame(line_items)
                        st.dataframe(df, use_container_width=True)
                    except Exception as e:
                        st.warning(f"Line items found but failed to display as table: {e}")
                else:
                    st.warning("No line items found or format is incorrect.")

                # Raw JSON output
                with st.expander("🔎 See Raw JSON"):
                    st.json(fields)
            else:
                st.error("❌ No fields extracted.")
    else:
        st.warning("OCR text not found.")
