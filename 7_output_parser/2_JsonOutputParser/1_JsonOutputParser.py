from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.5",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person\n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}    #additional format_instruction is used so that it tell the llm that in which format output is requried
)

# prompt = template.format()

# result = chat_model.invoke(prompt)  # return output in json format
# # print(result)

# result1 = parser.parse(result.content)   

# print(result1)

# print(type(result1))  # by default parser return dictionary 


#above is working fine but better to use chain

chain = template | chat_model | parser 

result = chain.invoke({})   # invoke() => always expect a dictionary so pass empty dict

print(result)

#biggest flaw is that jsonparser does not imply rigid schema, if you want then better to use StructuredOutputParser instead of JsonOutputParser