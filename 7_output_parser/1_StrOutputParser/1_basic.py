from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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
prompt1 = template1.invoke({'topic':"black hole"})

result = chat_model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = chat_model.invoke(prompt2)

print(result1.content)


"""
    too bulky to write and invoke after each content , can't be integrated with chains
"""