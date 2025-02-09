from fastapi import FastAPI
from pydantic import BaseModel
from src.chatbot import generate_response

app = FastAPI()

# Dictionary to store conversation history (Temporary memory)
conversation_memory = {}

class QueryRequest(BaseModel):
    user_id: str  #User id for tracking conversations
    query: str

@app.post("/ask")
def ask_question(request: QueryRequest):

    user_id = request.user_id  # Identify the user
    if user_id not in conversation_memory:
        conversation_memory[user_id] = []  # Initialize history for a new user
    # Append user query to history
    conversation_memory[user_id].append({"role": "user", "content": request.query})
    

    """FastAPI endpoint for chatbot Q&A."""
    response = generate_response(request.query)

     # Append chatbot response to history
    conversation_memory[user_id].append({"role": "assistant", "content": response})
    
    return {"query": request.query, "response": response}

# Run API with: uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload
