# 🧠 MemoryOS-AI Architecture

## Components

1. Memory Storage Layer
2. Ranking Engine
3. Context Manager
4. Compression Engine
5. Retrieval System

---

# 🔄 Memory Flow

User Input
    ↓
Memory Classification
    ↓
Compression
    ↓
Storage
    ↓
Retrieval
    ↓
Context Generation

---

# 🏗️ Core Modules

## memory_store.py
Handles persistent memory storage using SQLite.

## ranking_engine.py
Ranks memories using TF-IDF similarity scoring.

## retriever.py
Retrieves relevant memories based on query similarity.

## compression.py
Compresses long memories into smaller forms.

## context_manager.py
Builds optimized AI context from retrieved memories.

## streamlit_app.py
Provides dashboard visualization for stored memories.
