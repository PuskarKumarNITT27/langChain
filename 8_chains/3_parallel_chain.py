from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.5",
    task="text-generation"
)

llm2 = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

model1 = ChatHuggingFace(llm = llm1)
model2 = ChatHuggingFace(llm = llm2)



prompt1 = PromptTemplate(
    template= "Generate a note for the text: {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="generate 5 questions from the text: {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes','quiz']
)


parser = StrOutputParser()

parallel_chain = RunnableParallel(
    notes = prompt1 | model1 | parser,
    quiz = prompt2 | model2 | parser
)

merging_chain = prompt3 | model2 | parser 

final_chain  = parallel_chain | merging_chain 

text = """
Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It tries to find the best boundary known as hyperplane that separates different classes in the data. It is useful when you want to do binary classification like spam vs. not spam or cat vs. dog.

The main goal of SVM is to maximize the margin between the two classes. The larger the margin the better the model performs on new and unseen data.

Key Concepts of Support Vector Machine
Hyperplane: A decision boundary separating different classes in feature space and is represented by the equation wx + b = 0 in linear classification.
Support Vectors: The closest data points to the hyperplane, crucial for determining the hyperplane and margin in SVM.
Margin: The distance between the hyperplane and the support vectors. SVM aims to maximize this margin for better classification performance.
Kernel: A function that maps data to a higher-dimensional space enabling SVM to handle non-linearly separable data.
Hard Margin: A maximum-margin hyperplane that perfectly separates the data without misclassifications.
Soft Margin: Allows some misclassifications by introducing slack variables, balancing margin maximization and misclassification penalties when data is not perfectly separable.
C: A regularization term balancing margin maximization and misclassification penalties. A higher C value forces stricter penalty for misclassifications.
Hinge Loss: A loss function penalizing misclassified points or margin violations and is combined with regularization in SVM.
Dual Problem: Involves solving for Lagrange multipliers associated with support vectors, facilitating the kernel trick and efficient computation.
"""

result = final_chain.invoke({'text':text})

print(result)


final_chain.get_graph().print_ascii()


# for parallel chain , use RunnableParallel 