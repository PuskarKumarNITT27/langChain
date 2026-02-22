from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "MiniMaxAI/MiniMax-M2.5",
    task = "text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

chat_history = [
    SystemMessage(content = "you are a helpful AI assistant")
]

while True: 
    user_input = input("You : ")
    chat_history.append(HumanMessage(content = user_input))

    if user_input == "exit":
        break 
    
    result = chat_model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))

    print("AI : ",result.content)
