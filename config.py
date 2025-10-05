"""
Configuration loader.
"""

import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_MODEL = os.getenv("HUGGINGFACE_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
VECTOR_DIR = os.getenv("VECTOR_DIR", "data/faiss_index")
LOG_DIR = os.getenv("LOG_DIR", "logs/")
SEARCH_API = "duckduckgo"
