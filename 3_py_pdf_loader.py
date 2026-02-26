from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
""" 
    loading document using PyPDFLoader // start loading
    
    load only simple pdf using PyPDFLoader 
    
"""

loader = PyPDFLoader(file_path='10_document_loader/simple_pdf.pdf')
docs = loader.load()

print(docs)
print(len(docs))



# llm = HuggingFaceEndpoint(
#     repo_id='openai/gpt-oss-20b',
#     task='text-generation'
# )

# chat_model = ChatHuggingFace(llm = llm)

# prompt = PromptTemplate(
#     template='give me a summary about this text: \n{text}',
#     input_variables=['text']
# )

# parser = StrOutputParser()

# chain = prompt | chat_model | parser 

# result = chain.invoke({"text":docs[0].page_content})

# print(result)
