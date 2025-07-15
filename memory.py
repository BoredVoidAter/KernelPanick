
import json
import os

class AIMemory:
    def __init__(self, db_file="ai_memory.json"):
        self.db_file = db_file
        self.memory = self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {"entries": []}

    def _save_memory(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def store_info(self, content, tags=None):
        entry = {"content": content, "tags": tags if tags is not None else []}
        self.memory["entries"].append(entry)
        self._save_memory()
        return True

    def retrieve_info(self, query=None, tags=None):
        results = []
        for entry in self.memory["entries"]:
            match = True
            if query and query.lower() not in entry["content"].lower():
                match = False
            if tags:
                if not all(tag.lower() in [t.lower() for t in entry["tags"]] for tag in tags):
                    match = False
            if match:
                results.append(entry)
        return results

    def tag_info(self, index, new_tags):
        if 0 <= index < len(self.memory["entries"]):
            self.memory["entries"][index]["tags"].extend(new_tags)
            self._save_memory()
            return True
        return False

    def list_all(self):
        return self.memory["entries"]

