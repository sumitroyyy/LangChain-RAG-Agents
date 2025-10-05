"""
Chunk large texts into manageable parts.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(documents, chunk_size=300, overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_documents(documents)
