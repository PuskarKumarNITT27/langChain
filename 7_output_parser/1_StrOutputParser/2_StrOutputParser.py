from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm  = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.5",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="write a 5 line summary on the following text. \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | chat_model | parser | template2 | chat_model | parser

result = chain.invoke({'topic':"black hole"})

print(result)

"""
    StrOutputParser work with result.content only , and no need to specify result.content
"""