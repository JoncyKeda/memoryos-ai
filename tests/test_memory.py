from app.memory_engine import MemoryEngine

def test_store_memory():

    engine = MemoryEngine()

    engine.store_memory(
        "semantic",
        "Testing semantic memory storage."
    )

    memories = engine.store.fetch_all_memories()

    assert len(memories) > 0
