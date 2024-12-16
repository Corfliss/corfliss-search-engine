from fastapi import FastAPI, Query
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

@app.get("/search")
def search_items(query: str = Query("", min_length=1)) -> List[dict]:
    results = [
        item for item in dataset
        if query.lower() in item["name"].lower() or query.lower() in item["description"].lower()
    ]
    return results

# Wrap the FastAPI app with Mangum
handler = Mangum(app)
