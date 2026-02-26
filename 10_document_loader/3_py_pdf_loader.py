from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader ,UnstructuredPDFLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
""" 
    loading document using PyPDFLoader // start loading
"""
from pathlib import Path

pdf_path = Path(__file__).parent / "simple_pdf.pdf"
# print(type(pdf_path))
loader = PyPDFLoader(str(pdf_path))

docs = loader.load()
print(docs)

print(len(docs))

print(docs[0].page_content)
print(f"page 1 metadata: {docs[0].metadata}")

# # install => 'pip install unstructured pdfminer.six' for UnstructuredPDFLoader
# loader = UnstructuredPDFLoader(pdf_path)

# docs   = loader.load()

# print(len(docs))