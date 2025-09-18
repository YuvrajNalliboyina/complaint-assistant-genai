import streamlit as st
import requests

st.title("Internal Complaint Submission")

# Form fields
with st.form("complaint_form"):
    complaint_id = st.number_input("Complaint ID", min_value=1, step=1)
    product = st.text_input("Product")
    issue = st.text_input("Issue")
    company = st.text_input("Company", value="Bank of America")
    date_received = st.date_input("Date Received")
    submitted_via = st.selectbox("Submitted Via", ["Internal CRM", "Email", "Phone", "Chat"])
    complaint_what_happened = st.text_area("What Happened (Optional)")

    submitted = st.form_submit_button("Submit")

# POST to FastAPI
if submitted:
    data = {
        "complaint_id": complaint_id,
        "product": product,
        "issue": issue,
        "company": company,
        "date_received": str(date_received),
        "submitted_via": submitted_via,
        "complaint_what_happened": complaint_what_happened
    }

    response = requests.post("http://127.0.0.1:8000/submit_complaint", json=data)

    if response.status_code == 200:
        st.success("Complaint submitted successfully!")
    else:
        st.error(f"Failed to submit complaint. {response.text}")
