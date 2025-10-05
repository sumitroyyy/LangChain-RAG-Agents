"""
DataSight – CLI interface for your RAG agent.
Run: python main.py
"""

from agent.rag_agent import initialize_datasight_agent
from utils.logger import Logger

def main():
    log = Logger()
    agent = initialize_datasight_agent()
    log.info("Datasight started. Type 'exit' to quit.")

    chat_history = []
    while True:
        query = input("\nYou: ").strip()
        if query.lower() in ["exit", "quit"]:
            print("👋 Exiting Datasight.")
            break
        try:
            response = agent.run(query)
            print(f"\n🧠 Datasight: {response}")
            log.log_interaction(query, response)
        except Exception as e:
            log.error(f"Error: {e}")

if __name__ == "__main__":
    main()
