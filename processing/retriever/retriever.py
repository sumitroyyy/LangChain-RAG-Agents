"""
Retrieve top-k relevant chunks.
"""

def get_retriever(vector_store, k=4):
    return vector_store.as_retriever(search_type="mmr", search_kwargs={"k": k})
