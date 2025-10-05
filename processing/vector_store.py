"""
Create and manage FAISS vector store.
"""

import os
from langchain.vectorstores import FAISS

def build_vector_store(chunks, embedding_model, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    vector_store = FAISS.from_documents(chunks, embedding_model)
    vector_store.save_local(save_dir)
    return vector_store

def load_vector_store(embedding_model, save_dir):
    return FAISS.load_local(save_dir, embedding_model)
