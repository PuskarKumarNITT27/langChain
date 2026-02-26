# install : 'pip install langchain-experimental'
 
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

embed_model =HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

text_splitter = SemanticChunker(
    embed_model,
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=3
)

text = """
Space exploration has always fascinated humanity. From the first satellite launched into orbit to modern interplanetary missions, our understanding of the universe continues to expand. Scientists are now planning missions to Mars, hoping to establish a sustainable human presence on the red planet.

Artificial Intelligence is transforming industries across the globe. Machine learning algorithms can analyze massive datasets in seconds, helping businesses make smarter decisions. Large language models are capable of understanding and generating human-like text, making them useful in customer support, education, and research.

Climate change remains one of the biggest challenges facing our planet. Rising global temperatures are causing glaciers to melt and sea levels to rise. Governments and organizations are investing in renewable energy sources like solar and wind to reduce carbon emissions and protect ecosystems.

Music has a powerful effect on human emotions. Listening to certain types of music can reduce stress and improve concentration. Researchers have found that rhythm and melody can stimulate different regions of the brain, influencing mood and memory.

The human brain is one of the most complex organs in the body. It contains billions of neurons that communicate through electrical and chemical signals. Neuroscientists continue to study how memory, creativity, and consciousness emerge from neural activity.
"""

docs = text_splitter.create_documents(text)

print(len(docs))

# print(docs)
print(docs[0].page_content)