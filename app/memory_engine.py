from app.memory_store import MemoryStore
from app.retriever import Retriever
from app.context_manager import ContextManager
from app.compression import MemoryCompression
from app.utils import current_timestamp

class MemoryEngine:

    def __init__(self):

        self.store = MemoryStore()

        self.retriever = Retriever()

        self.context_manager = ContextManager()

        self.compressor = MemoryCompression()

    def calculate_importance(self, content):

        score = min(len(content.split()) / 50, 1.0)

        return round(score, 2)

    def store_memory(self, memory_type, content):

        compressed = self.compressor.compress(content)

        memory = {
            "memory_type": memory_type,
            "content": compressed,
            "importance": self.calculate_importance(content),
            "timestamp": current_timestamp()
        }

        self.store.insert_memory(memory)

        print(f"✅ Stored {memory_type} memory.")

    def retrieve_relevant_memories(self, query):

        memories = self.store.fetch_all_memories()

        ranked = self.retriever.retrieve(query, memories)

        return ranked

    def generate_context(self, query):

        ranked = self.retrieve_relevant_memories(query)

        context = self.context_manager.build_context(ranked)

        return context
