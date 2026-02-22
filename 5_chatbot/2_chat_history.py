from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.5",
    task = "text-generation"
)
chat_model = ChatHuggingFace(llm= llm)

chat_history = []

while True: 
    user_input = input("You : ")
    chat_history.append(user_input)

    if user_input == "exit":
        break
    result = chat_model.invoke(user_input)
    chat_history.append(result.content)
    print("AI : ",result.content)

print(chat_history)