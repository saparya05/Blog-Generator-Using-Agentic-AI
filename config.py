from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
import streamlit as st

load_dotenv()

llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]
)
