"""
Generate embeddings using SentenceTransformers (Hugging Face).
"""

from langchain.embeddings import SentenceTransformerEmbeddings

def get_embedding_model(model_name):
    return SentenceTransformerEmbeddings(model_name=model_name)
