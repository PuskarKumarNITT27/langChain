"""
    static prompting 
"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.5",
    task = "text-generation"
)
chat_model = ChatHuggingFace(llm= llm)

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summerize"):
    result = chat_model.invoke(user_input)
    st.write(result.content)
