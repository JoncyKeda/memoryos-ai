from app.memory_engine import MemoryEngine

def main():

    engine = MemoryEngine()

    print("\n🧠 MemoryOS-AI Started\n")

    engine.store_memory(
        memory_type="semantic",
        content="User is learning reinforcement learning and deep learning."
    )

    engine.store_memory(
        memory_type="episodic",
        content="User previously built an AI recommendation system."
    )

    query = "Give reinforcement learning project ideas"

    results = engine.retrieve_relevant_memories(query)

    print(f"\n🔍 Query: {query}\n")

    for memory, score in results:
        print(f"Memory: {memory[2]}")
        print(f"Similarity Score: {round(score, 2)}")
        print("-" * 50)

if __name__ == "__main__":
    main()
