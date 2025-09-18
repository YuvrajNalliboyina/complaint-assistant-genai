import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to Supabase DB
db_url = os.getenv("DB_URL")
conn = psycopg2.connect(db_url)

# Fetch data from table
query = "SELECT * FROM cfpb_complaints;"
df = pd.read_sql(query, conn)

# Preview results
print(df.head())
conn.close()
