import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
DB_URL = os.getenv("DB_URL")

# Load cleaned CSV
csv_path = "C:/Users/phani/Documents/complaint-assistant-genai/data/cfpb_bankofamerica_cleaned.csv"
df = pd.read_csv(csv_path)

# Add source column if missing
if "source" not in df.columns:
    df["source"] = "cfpb"

# Upload data to Supabase Postgres
def upload_data(df):
    try:
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO cfpb_complaints (
                    date_received, company, complaint_what_happened, product, sub_product, issue,
                    submitted_via, state, company_public_response, timely, date_sent_to_company, zip_code, tags, has_narrative, consumer_consent_provided, consumer_disputed, sub_issue, company_response 
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
            """, tuple(row))
        
        conn.commit()
        print(f"Uploaded {len(df)} rows.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Upload failed:", e)

if __name__ == "__main__":
    upload_data(df)
