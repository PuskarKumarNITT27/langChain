from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda

#RunnableLambda => convert python function to runnable

def word_count(text):
    return len(text.split())

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="generate me a joke on {topic}",
    input_variables=['topic']
)

seq_chain = RunnableSequence(prompt, chat_model,parser)

# way 1 
# parallel_chain  = RunnableParallel({
#     "joke": RunnablePassthrough(),
#     "word_count": RunnableLambda(word_count)
# })

# way 2
parallel_chain  = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(lambda x: len(x.split()))
})

final_chain = RunnableSequence(seq_chain,parallel_chain)

result = final_chain.invoke({"topic":"AI"})

print(result)