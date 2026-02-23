from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.5",
    task="text-generation",
    temperature=0.8  # temperature enforces randomness 
)

chat_model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name: str = Field(description="name of the person")
    age: int = Field(gt=18, description="age of the person")
    city: str= Field(description="Name of the city the person belong to ")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="generate the name,age and city of a fictional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'place':"indian"})

# print(prompt)
# result = chat_model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
# print(final_result.model_dump_json())

#better way using chain

chain = template | chat_model | parser 

result = chain.invoke({'place':"india"})

print(result)