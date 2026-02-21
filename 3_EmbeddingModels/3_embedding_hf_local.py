from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

# single query embedding
# text = "What is the capital of India"

# result = embedding.embed_query(text)


# multiple query embedding generation 

documents = [
    "What is the capital of India",
    "who is the prime minister of India",
    "What is the mean of Embedding"
]

result = embedding.embed_documents(documents)

print(str(result))



"""
    1. this is local embedding model 
    2. first install sentence-transformer => pip install sentence-transformer
    3. run the code it will automatically install locally and then generate embeddings
"""