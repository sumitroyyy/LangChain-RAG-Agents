"""
JSON + console logger.
"""

import json, os, datetime

class Logger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, "datasherpa_logs.json")

    def _write(self, entry):
        with open(self.log_file, "a") as f:
            json.dump(entry, f)
            f.write("\n")

    def info(self, msg):
        print(f"[INFO] {msg}")

    def error(self, msg):
        print(f"[ERROR] {msg}")

    def log_interaction(self, query, response):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "query": query,
            "response": response,
        }
        self._write(entry)
