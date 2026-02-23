from langchain_core.prompts import ChatPromptTemplate

# method 1: 
# from langchain_core.messages import SystemMessage, HumanMessage 

# chat_template = ChatPromptTemplate([
#     SystemMessage(content= 'You are a helpful {domain} expert'),
#     HumanMessage(content = 'Explain in simple terms, what is {topic}')
# ])


# method 2: 
# chat_template  = ChatPromptTemplate.from_messages([
#     ('system',"you are a helpful {domain} expert"),
#     ('human' , "Explain in simple terms , what is {topic}")
# ])


# method 3: 

chat_template  = ChatPromptTemplate([
    ('system',"you are a helpful {domain} expert"),
    ('human' , "Explain in simple terms , what is {topic}")
])

prompt = chat_template.invoke({'domain':"cricketer",'topic':"Dusra"})

print(prompt)