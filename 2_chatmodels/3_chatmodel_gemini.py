from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

result = chat_model.invoke("enter your question ")

print(result.content)


#api key in format: GOOGLE_API_KEY = "your_api_key"