from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.5",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

template = PromptTemplate(
    template="generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = template | chat_model | parser

result = chain.invoke({"topic":"India"})

print(result)

chain.get_graph().print_ascii() # for printing chain

#install 'pip install grandalf' before using get_graph()