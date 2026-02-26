from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from pathlib import Path

loader = DirectoryLoader(
    path='10_document_loader/books/',
    glob='*.pdf',
    loader_cls=PyPDFLoader 
)

# DirectoryLoader loads whole document as a single document

# docs = loader.load()

# print(len(docs))

# print(docs[3].page_content)
# print(docs[3].metadata)


docs =  loader.lazy_load()

for doc in docs: 
    print(doc.metadata)



""" 
use lazy_load , as it load one document at a time
"""