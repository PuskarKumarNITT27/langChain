from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template="generate me a joke on: {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='explain me the joke {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

sequence_chain = RunnableSequence(prompt1 ,chat_model,parser)

parallel_chain = RunnableParallel({
    "print_joke": RunnablePassthrough(),
    "explain_joke" : RunnableSequence(prompt2,chat_model,parser)
})

combined_chain = RunnableSequence(sequence_chain,parallel_chain)

result   = combined_chain.invoke({"topic": "AI"})

print(result)



#RunnablePassthrough => simply output given input, it means it does nothing