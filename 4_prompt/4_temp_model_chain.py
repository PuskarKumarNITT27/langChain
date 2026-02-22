from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate ,load_prompt

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="MiniMaxAI/MiniMax-M2.5",
#     task = "text-generation"
# )

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=1024
) 

chat_model = ChatHuggingFace(llm= llm)


# input section 

st.header("Research Tool")

paper_input = st.selectbox("Select research paper name: ", ["select ...","Attention is All You Need","BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: Language Models are Few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style: ",["Beginner-Friendly","Technical","code-oriented","Mathematical"])

length_input = st.selectbox("Select Explanation Length: ",["Short (1-2 paragraph)" , "Medium (3-5 paragraph)","Long (detailed explanation)"])


# prompt template 

template = load_prompt('template.json')


if st.button("Summerize"):

    chain = ( template | chat_model )
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result.content)
