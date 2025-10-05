# 🧠 DataSight
A CLI Retrieval-Augmented Generation (RAG) Agent powered by LangChain + Hugging Face + FAISS + DuckDuckGo.

## 🔧 Features
- Load PDFs and create FAISS index
- Query local knowledge or fallback to web
- Logs all Q&A interactions as JSON

## Architecture
PDFs → Chunks → Embeddings → FAISS
             ↓
        Retriever → Agent
             ↓
    [LLM Answer + Sources]

## Tech Stack

Python 3.10+

LangChain

FAISS (local vector DB)

SentenceTransformers (all-MiniLM-L6-v2)

OpenAI or HuggingFace LLM

DuckDuckGo Search API for web fallback

dotenv + logging

## Files

main.py → Entry point (interactive CLI chat loop)

pdf_loader.py → Load & clean text from PDFs

chunker.py → Recursive text splitting

embeddings.py → Create embeddings with SentenceTransformers

vector_store.py → Build, save, and load FAISS index

retriever.py → Retrieve top-k relevant chunks

tools.py → Define RAG_QA and DuckDuckGo web search tools

rag_agent.py → LangChain Agent setup

logger.py → JSON + console logging utility

README.md → Full setup, usage, and examples

requirements.txt, .env.example, Dockerfile

## 🚀 Quick Start
```bash
git clone <your_repo_url>
cd datasherpa
pip install -r requirements.txt
cp .env.example .env
python main.py




