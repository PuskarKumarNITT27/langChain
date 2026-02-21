from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model = "gpt-4",temperature=1.2, max_completion_tokens=50)

result = chat_model.invoke("your question => like what is the capital of India")

print(result)


# input : string, output: json data contain content, ....
# for simple output : use print(result.content)