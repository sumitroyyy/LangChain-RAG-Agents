"""
Module to load and clean PDF files.
"""

import os
from langchain.document_loaders import PyPDFLoader

def load_pdfs(folder_path):
    documents = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, file))
            documents.extend(loader.load())
    return documents
