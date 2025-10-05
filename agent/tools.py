"""
Define available agent tools.
"""

from langchain.agents import Tool

def get_tools(qa_chain, web_search_fn):
    return [
        Tool(name="RAG_QA", func=qa_chain.run, description="Answer from local documents"),
        Tool(name="Web_Search", func=web_search_fn, description="Search online using DuckDuckGo"),
    ]
