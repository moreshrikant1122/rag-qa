import os
# from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader,UnstructuredMarkdownLoader
from pathlib import Path


def load_documents(folder_path):
    """Load all markdown files from the folder."""
    mixed_loader = DirectoryLoader(
    path=folder_path,
    glob="*.md",
    loader_cls=UnstructuredMarkdownLoader,
    recursive=True,
    )
    
    docs = mixed_loader.load()

    return docs

if __name__ == "__main__":
    path = (Path.cwd() / "data/").resolve()
    docs = load_documents(path)
    print(f"Loaded {len(docs)} documents.")
