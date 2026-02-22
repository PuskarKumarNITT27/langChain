from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "MiniMaxAI/MiniMax-M2.5",
    task = "text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

class Review(TypedDict):
    summary: str 
    sentiment: str 

structured_output = chat_model.with_structured_output(Review)

result = structured_output.invoke("""
    The hardware is great,but the software feels bloated. There are too many pre-installed apps that I can't remove . Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
""")
print(result)
print(result['sentiment'])