from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI app with docs and title
app = FastAPI(
    title="Complaint Submission API",
    description="Submit internal CRM complaints",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# In-memory storage
complaint_store: List[dict] = []

# Define complaint schema
class Complaint(BaseModel):
    complaint_id: int
    product: str
    issue: str
    company: str
    date_received: str
    submitted_via: Optional[str] = "Internal CRM"
    complaint_what_happened: Optional[str] = None

# Health check endpoint
@app.get("/")
def root():
    return {"message": "API is working!"}

# Submit complaint endpoint
@app.post("/submit_complaint")
def submit_complaint(complaint: Complaint):
    complaint_store.append(complaint.model_dump())
    return {
        "status": "success",
        "message": "Complaint received",
        "total_complaints": len(complaint_store)
    }

# Optional: Retrieve all submitted complaints
@app.get("/complaints")
def get_complaints():
    return complaint_store
if __name__ == "__main__":
    import uvicorn
    print("Swagger UI: http://127.0.0.1:8000/docs")
    print("ReDoc UI:   http://127.0.0.1:8000/redoc")
    uvicorn.run("crm_api:app", host="127.0.0.1", port=8000, reload=True)
