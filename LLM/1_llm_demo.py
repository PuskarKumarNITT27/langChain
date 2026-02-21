
#LLM models => you have to be an OPENAI_API_KEY = "your_api_key" , paid only

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")


result = llm.invoke("write your question like `what is the capital of india`")

print(result)


# LLM format input: string, output: string