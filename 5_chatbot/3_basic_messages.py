from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "MiniMaxAI/MiniMax-M2.5",
    task= "text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

messages = [
    SystemMessage(content="You are a helpful assistance"),
    HumanMessage(content = "Tell me about LangChain")
]

result = chat_model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)