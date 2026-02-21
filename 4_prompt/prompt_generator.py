from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template = """
        Please summerize the research paper titled "{paper_input}" with the following specifications: 
        Explanation style: {style_input}
        Explanation length : {length_input}
        1. Mathematical details: 
            - include relevant mathematical equations if present in the paper 
            - explain the mathematical concepts using simple, intuitive code snippets where applicable.

        2. Analogies: 
            - use relatable analogies to simplify complex ideas.
        
        if certain information is not available in the paper, respond with : "insufficient information available" instead of Guessing.
        Ensure the summar is clear,accurate and aligned with the provided style and length.
    """,
    input_variables = ['paper_input','style_input','length_input']
)

template.save('template.json')