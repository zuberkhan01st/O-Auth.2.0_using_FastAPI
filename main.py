import os
import requests
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# FatSecret API Credentials
FATSECRET_CLIENT_ID = os.getenv("FATSECRET_CLIENT_ID")
FATSECRET_CLIENT_SECRET = os.getenv("FATSECRET_CLIENT_SECRET")
FATSECRET_BASE_URL = os.getenv("FATSECRET_BASE_URL")
FATSECRET_API_URL = os.getenv("FATSECRET_API_URL")

app = FastAPI()

def get_access_token():
    """Obtain OAuth 2.0 access token from FatSecret API."""
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "basic",
        "client_id": FATSECRET_CLIENT_ID,
        "client_secret": FATSECRET_CLIENT_SECRET
    }
    response = requests.post(FATSECRET_BASE_URL, data=data, headers=headers)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Error getting access token: {response.text}")

@app.get("/")
def home():
    return {"message": "FatSecret API Integration with FastAPI & OAuth 2.0"}

@app.get("/search_foods")
def search_foods(query: str = Query(..., description="Food name to search"), max_results: int = 10, page_number: int = 0):
    """Search for food items using the FatSecret API."""
    access_token = get_access_token()

    params = {
        "method": "foods.search",
        "format": "json",
        "search_expression": query,
        "max_results": max_results,
        "page_number": page_number
    }
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(FATSECRET_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching food data")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
