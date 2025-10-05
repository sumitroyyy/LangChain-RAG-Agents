"""
Utility helpers such as web search.
"""

from duckduckgo_search import DDGS

def duckduckgo_search(query):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
        snippets = [r["body"] for r in results]
        return "\n".join(snippets) if snippets else "No online info found."
