import os
from langchain.document_loaders import TextLoader

def load_documents(folder_path):
    """Load all markdown files from the folder."""
    docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".md"):  # Process only markdown files
            loader = TextLoader(os.path.join(folder_path, file))
            docs.extend(loader.load())
    return docs

if __name__ == "__main__":
    docs = load_documents("../data")
    print(f"Loaded {len(docs)} documents.")
