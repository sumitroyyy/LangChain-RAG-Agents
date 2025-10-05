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

## 🚀 Quick Start
```bash
git clone <your_repo_url>
cd datasherpa
pip install -r requirements.txt
cp .env.example .env
python main.py




