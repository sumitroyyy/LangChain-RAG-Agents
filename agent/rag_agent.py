"""
Initialize LangChain agent with local retriever + web search fallback.
"""

from langchain.agents import initialize_agent
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from processing.embeddings import get_embedding_model
from processing.vector_store import load_vector_store
from retriever.retriever import get_retriever
from agent.tools import get_tools
from utils.helper import duckduckgo_search
from config import HUGGINGFACE_MODEL, VECTOR_DIR

def initialize_datasherpa_agent():
    embedding_model = get_embedding_model(HUGGINGFACE_MODEL)
    vector_store = load_vector_store(embedding_model, VECTOR_DIR)
    retriever = get_retriever(vector_store)

    llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct", model_kwargs={"temperature": 0.2})
    qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever)
    tools = get_tools(qa_chain, duckduckgo_search)

    return initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=False)
