from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
import uvicorn

app = FastAPI()

# Define API Key
API_KEY = "test12345"  # Change this to a secure API key
api_key_header = APIKeyHeader(name="X-API-Key")

# Sample Data with Supervisor
employees = [
    {
        "ID": 200,
        "FirstName": "Melinda",
        "LastName": "Sipos",
        "JobTitle": "Senior Technical Account Manager",
        "Department": "Technical Account Management",
        "Location": "New York",
        "Email": "melinda.sipos@picklinet.onmicrosoft.com",
        "Supervisor": "John Doe"
    },
    {
        "ID": 201,
        "FirstName": "Lipot",
        "LastName": "Pickermann",
        "JobTitle": "Platform Engineer",
        "Department": "Platform Engineering",
        "Location": "New York",
        "Email": "lipot.pickermann@beacon.io",
        "Supervisor": "Raj Atwal"
    },
   
]

# API Key Dependency
def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/employees", dependencies=[Depends(verify_api_key)])
def get_employees():
    return employees

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
