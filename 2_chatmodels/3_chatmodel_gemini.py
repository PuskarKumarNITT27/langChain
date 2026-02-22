from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

result = chat_model.invoke("what is the capital of india ")

print(result.content[0]['text'])


#api key in format: GOOGLE_API_KEY = "your_api_key"