from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents = [
    "embedding text 1",
    "embedding text 2",
    "embedding text 3"
]

result = embedding.embed_documents(documents)

print(str(result))


#embedding generation for multiple query at the same time