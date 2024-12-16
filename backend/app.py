from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from mangum import Mangum

dataset = [
    {"id": 1, "name": "Apple", "description": "A juicy red fruit."},
    {"id": 2, "name": "Banana", "description": "A sweet yellow fruit."},
    {"id": 3, "name": "Cherry", "description": "A small red fruit."},
    {"id": 4, "name": "Date", "description": "A sweet brown fruit."},
    {"id": 5, "name": "Elderberry", "description": "A small dark fruit."},
]

app = FastAPI()

# List of allowed origins (replace with your frontend URL)
origins = [
    "https://corfliss-search-engine.vercel.app",  # Frontend URL
    "http://localhost:3000",             # If testing locally
]

# Add CORS middleware to allow requests from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],    # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],    # Allows all headers
)

@app.get("/search")
async def search(query: str):
    # Filter data based on the query
    results = [item for item in dataset if query.lower() in item["name"].lower()]
    return results

# Wrap the FastAPI app with Mangum
handler = Mangum(app)
