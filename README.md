**Q&A Chatbot with FastAPI and Vector Store**

A Q&A Chatbot that uses FAISS as a vector store and OpenAI GPT for generating responses based on Ubuntu documentation.
Features
 Retrieval-Augmented Generation (RAG): Retrieves relevant documents before answering.
 Supports FAISS : Vector store for efficient document search.
 FastAPI Backend: Deploys as a REST API with Swagger UI (/docs).
 Conversation Memory: Remembers previous queries for contextual conversations.


**Chunking Strategy**
I am using Recursive Character Text Splitter from LangChain, which:
 Splits text into overlapping chunks
 Ensures better retrieval context
 Prevents cutting off meaningful sections

