import openai
import os
from dotenv import load_dotenv
from vector_store import load_vector_store,retrieve_documents

# Load API Key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

vector_store = load_vector_store("models/faiss_index")

def generate_response(query, stream=False):
    """Retrieve relevant documents and generate an AI response."""
    retrieved_docs = retrieve_documents(vector_store=vector_store, query=query)
    context = " ".join(retrieved_docs)  # Combine retrieved docs

    prompt = f"Context: {context}\nUser Question: {query}\nAI Answer:"

    response = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[{"role": "user", "content": prompt}],
        stream=stream
        )
    
    if stream:
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
        return
    
    return response.choices[0].message.content

# Running in CLI
if __name__ == "__main__":
    print("Starting Demo chatbot...")

    print("Chatbot CLI - Type 'exit' to quit")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chatbot. Goodbye!")
            break
        response = generate_response(user_input, True)
        

