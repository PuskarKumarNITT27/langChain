from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template="generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a linkedein post about topic {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain =RunnableParallel({
    "tweet": prompt1 | chat_model | parser,
    "linkedein": prompt2 | chat_model | parser
})

result  = parallel_chain.invoke({"topic":"AI"})

print(result)