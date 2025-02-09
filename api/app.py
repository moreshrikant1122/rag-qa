from fastapi import FastAPI
from pydantic import BaseModel
from src.chatbot import generate_response

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
def ask_question(request: QueryRequest):

    """FastAPI endpoint for chatbot Q&A."""
    response = generate_response(request.query)

    return {"query": request.query, "response": response}

# Run API with: uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload
