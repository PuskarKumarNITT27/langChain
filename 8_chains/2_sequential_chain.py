# userInput (topic) => llm => report => llm => 5 line summary
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

template = PromptTemplate(
    template="give me a detailed information on topic : {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="give me 5 line summary of the content: {content}",
    input_variables=['content']
)

parser = StrOutputParser()

chain = template | chat_model | parser | template2 | chat_model | parser 

result = chain.invoke({'topic':"cricket"})

print(result)

chain.get_graph().print_ascii()  # for visual depection of chain