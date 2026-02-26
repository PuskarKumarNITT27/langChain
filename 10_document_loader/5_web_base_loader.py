from langchain_community.document_loaders import WebBaseLoader


""" 
    works very well with static webpages , use seleneium if dynamic webpage is there
    => you can pass a list of urls 
"""

# url = 'https://docs.langchain.com/oss/javascript/integrations/document_loaders/file_loaders/directory'

# loader = WebBaseLoader(url)

# docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)


url_list = [
    'https://docs.langchain.com/oss/javascript/integrations/document_loaders/file_loaders/directory',
    'https://docs.langchain.com/oss/python/integrations/providers/overview'
]
 
loader = WebBaseLoader(url_list)

docs = loader.load()

print(len(docs))

print(docs[1].metadata)