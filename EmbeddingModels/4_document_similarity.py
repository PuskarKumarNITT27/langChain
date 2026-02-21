from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is an Indian Cricketer known for his aggressive batting and leadership",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills",
    "Sachin Tendulkar , also know as the 'God of Criket' , holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers"
]

query = 'tell me about Virat Bumrah'

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

result = cosine_similarity([query_embeddings],doc_embeddings)  # pass both as 2D vectors

result = result[0]
scores = list(enumerate(result))  # keeps (index, score) pair intact , so we can sort

print(scores)

#sorting on the basis of second item

sorting = sorted(scores,key=lambda x:x[1])

print(sorting)

index,score = sorting[-1]

print(f"document with highest similarity is : {documents[index]}")

