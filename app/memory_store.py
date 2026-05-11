import sqlite3

DB_PATH = "data/memories.db"

class MemoryStore:

    def __init__(self):

        self.conn = sqlite3.connect(DB_PATH)

        self.create_table()

    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            memory_type TEXT,
            content TEXT,
            importance REAL,
            timestamp TEXT
        )
        """

        self.conn.execute(query)

        self.conn.commit()

    def insert_memory(self, memory):

        query = """
        INSERT INTO memories(memory_type, content, importance, timestamp)
        VALUES (?, ?, ?, ?)
        """

        self.conn.execute(query, (
            memory["memory_type"],
            memory["content"],
            memory["importance"],
            memory["timestamp"]
        ))

        self.conn.commit()

    def fetch_all_memories(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM memories")

        return cursor.fetchall()
