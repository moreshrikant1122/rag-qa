import os
import faiss
import numpy as np
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS, Chroma
from pathlib import Path
from langchain_community.docstore.in_memory import InMemoryDocstore
from uuid import uuid4

# Load documents
from src.load_data import load_documents

# Step 1: Load Data & Split into Chunks
def chunk_documents(docs, chunk_size=512, chunk_overlap=50):
    """Splits documents into smaller chunks for better retrieval."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(docs)


# Step 3: Create FAISS Vector Store
def create_faiss_store():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={},
    )

    return vector_store

def add_documents_to_vector_store(vector_store, chunks):
    uuids = [str(uuid4()) for _ in range(len(chunks))]

    vector_store.add_documents(documents=chunks, ids=uuids)

    ids = vector_store.save_local("/home/justdial/Desktop/rag_project/qa-chatbot/models/faiss_index")

    return ids


def load_vector_store(store_path):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    new_vector_store = FAISS.load_local(
    store_path, embeddings, allow_dangerous_deserialization=True
    )

    return new_vector_store

def retrieve_documents(vector_store, query, top_k=3):
    """Retrieve top K relevant documents from the vector store."""
    results = vector_store.similarity_search(query, k=top_k)
    return [doc.page_content for doc in results]



if __name__ == "__main__":
    path = (Path.cwd() / "data/").resolve()

    docs = load_documents(path)
    chunks = chunk_documents(docs)

    print("Creating FAISS Vector Store...")
    faiss_store = create_faiss_store(chunks)

    print("Vector store created successfully!")
