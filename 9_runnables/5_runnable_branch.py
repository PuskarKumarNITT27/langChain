from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda,RunnableBranch

# RunnableBranch => used for branching condition pass in tuple (condition,chain)
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="write a detailed report on topic {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summerize the following text \n{text}',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt, chat_model,parser)

branch_chain = RunnableBranch(
    # (condition, runnable)
    (lambda x: len(x.split() )> 500,RunnableSequence(prompt2,chat_model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)

result = final_chain.invoke({"topic":"russia vs ukaraine"})

print(result)