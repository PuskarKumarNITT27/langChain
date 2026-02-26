# install langchain-community => pip install langchain-community
from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path='./requirements.txt')
docs = loader.load()

print(docs)
print(len(docs))

print(f"Content: {docs[0].page_content}")
print(f"metadata: {docs[0].metadata}")
""" 
    1. loader.load() => returns python list 
    2. two important attribute , page_content, metadata

"""