from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model = "gemini-3-flash-preview")

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me information about topic: {topic}\n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}    #additional format_instruction is used so that it tell the llm that in which format output is requried
)


chain = template | chat_model | parser 

result = chain.invoke({'topic':"black Hole"})   # invoke() => always expect a dictionary so pass empty dict

print(result)

#biggest flaw is that jsonparser does not imply rigid schema, if you want then better to use StructuredOutputParser instead of JsonOutputParser