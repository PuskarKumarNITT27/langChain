from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.5",
    task = "text-generation"
)
chat_model = ChatHuggingFace(llm= llm)

question = "what is the capital of india"
result = chat_model.invoke(question)

print(f"Question: {question}")
print(f"Answer: {result.content}")

#api key format hugging face:  HUGGINGFACEHUB_API_TOKEN = "your access token"