# ingestion/simulated_crm.py

import requests
import time
import random

# Sample complaint data pool
sample_complaints = [
    {
        "complaint_id": 90001,
        "product": "Credit card",
        "issue": "Unauthorized transactions",
        "company": "BANK OF AMERICA, NATIONAL ASSOCIATION",
        "date_received": "2025-07-25",
        "submitted_via": "CRM",
        "complaint_what_happened": "Customer reports suspicious charges not made by them."
    },
    {
        "complaint_id": 90002,
        "product": "Checking account",
        "issue": "Fees or charges",
        "company": "BANK OF AMERICA, NATIONAL ASSOCIATION",
        "date_received": "2025-07-25",
        "submitted_via": "CRM",
        "complaint_what_happened": "Unexpected monthly maintenance fee charged despite balance requirements."
    },
    {
        "complaint_id": 90003,
        "product": "Mortgage",
        "issue": "Loan servicing, payments, escrow account",
        "company": "BANK OF AMERICA, NATIONAL ASSOCIATION",
        "date_received": "2025-07-25",
        "submitted_via": "CRM",
        "complaint_what_happened": "Escrow account miscalculation led to incorrect payment notice."
    }
]

# Simulate sending complaints one by one
for complaint in sample_complaints:
    try:
        response = requests.post("http://127.0.0.1:8000/submit_complaint", json=complaint)
        print(f"[{complaint['complaint_id']}] Status: {response.status_code} | {response.json()}")
        time.sleep(random.uniform(1, 3))  # Simulate delay between submissions
    except Exception as e:
        print(f"Failed to send complaint {complaint['complaint_id']}: {e}")
