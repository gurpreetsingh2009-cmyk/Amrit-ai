class RobustMemory:
    def __init__(self):
        self.memory = []  # List to store memory items
        self.version = 0  # Version control for memory items
        self.timeline = []  # Timeline of memory operations

    def save_memory(self, item, priority=1):
        self.memory.append({'item': item, 'version': self.version, 'priority': priority})
        self.version += 1
        self.timeline.append({'action': 'saved', 'item': item, 'version': self.version, 'timestamp': '2026-02-27 14:53:03'})

    def recall_memory(self):
        return self.memory

    def search_memory(self, query):
        results = [m for m in self.memory if query in m['item']]
        return results

    def delete_memory(self, item):
        self.memory = [m for m in self.memory if m['item'] != item]
        self.timeline.append({'action': 'deleted', 'item': item, 'timestamp': '2026-02-27 14:53:03'})

    def get_memory_stats(self):
        return {'total_memory_items': len(self.memory), 'version': self.version}

    def persist_to_disk(self, file_name):
        import json
        with open(file_name, 'w') as f:
            json.dump(self.memory, f)

    def load_from_disk(self, file_name):
        import json
        with open(file_name, 'r') as f:
            self.memory = json.load(f)

    def export_memory(self):
        return self.memory

    def import_memory(self, memory_data):
        self.memory.extend(memory_data)

    def clear_memory(self):
        self.memory = []

    def get_memory_timeline(self):
        return self.timeline

    def get_memory_by_priority(self, priority):
        return [m for m in self.memory if m['priority'] == priority]