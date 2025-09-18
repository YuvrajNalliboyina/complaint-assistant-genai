import streamlit as st
import requests

st.set_page_config(page_title="Email Complaint Entry", layout="centered")
st.title("📧 Submit Free-Text Complaint")

text = st.text_area("Describe your complaint:")
if st.button("Submit Complaint"):
    if not text.strip():
        st.warning("Please enter a complaint.")
    else:
        payload = {
            "complaint_id": 9999,
            "product": "Credit reporting",
            "issue": "Incorrect information on credit report",
            "company": "Sample Company",
            "date_received": "2025-07-25",
            "complaint_what_happened": text
        }

        try:
            response = requests.post("http://127.0.0.1:8000/submit_complaint", json=payload)
            if response.status_code == 200:
                st.success("Complaint submitted successfully!")
            else:
                st.error("Failed to submit complaint.")
        except Exception as e:
            st.error(f"Error: {e}")
