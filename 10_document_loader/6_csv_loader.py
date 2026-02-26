from langchain_community.document_loaders import CSVLoader
from pathlib import Path

dir_path = Path(__file__).parent / "data.csv"

loader = CSVLoader(str(dir_path))

docs = loader.load()

print(len(docs))
print(docs[2].page_content)

print(docs[0].page_content)
print(docs[2].metadata)



""" 
    note : you can design custom data loader , see documentation
"""