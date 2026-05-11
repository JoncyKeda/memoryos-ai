import streamlit as st
import pandas as pd

from app.memory_store import MemoryStore

st.set_page_config(
    page_title="MemoryOS-AI Dashboard",
    layout="wide"
)

st.title("🧠 MemoryOS-AI Dashboard")

store = MemoryStore()

memories = store.fetch_all_memories()

if memories:

    df = pd.DataFrame(
        memories,
        columns=[
            "ID",
            "Memory Type",
            "Content",
            "Importance",
            "Timestamp"
        ]
    )

    st.subheader("📋 Stored Memories")

    st.dataframe(df)

    st.subheader("📊 Importance Scores")

    st.bar_chart(df["Importance"])

else:
    st.warning("No memories stored yet.")
