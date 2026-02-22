# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict , Annotated ,Optional ,Literal
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field 

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")


# llm = HuggingFaceEndpoint(
#     repo_id = "MiniMaxAI/MiniMax-M2.5",
#     task = "text-generation"
# )

# chat_model = ChatHuggingFace(llm = llm)

#schmea
json_schema = {
    "title":"Review",
    "type":"object",
    "properties":{
        "key_themes":{
            "type":"array",
            "items":{
                "type":"string"
            },
            "description":"write down all the key themes discussed in the review in a list"
        },
        "summary":{
            "type":"string",
            "description": "A brief summary of the review"
        },
        "sentiment":{
            "type":"string",
            "enum":["pos","neg"],
            "description":"Return sentiment of the review either negative,positive or neutral"
        },
        "pros":{
            "type":["array","null"],
            "items":{
                "type":"string"
            },
            "description":"Write down all the pros inside a list"
        },
        "cons":{
            "type":["array","null"],
            "items":{
                "type":"string"
            },
            "description":"Write down all the cons inside a list"
        }
    }
}  
structured_output = chat_model.with_structured_output(json_schema)

result = structured_output.invoke("""
    I recently upgraded to the samsung galaxy s24 ultra, and i must say, it's an absolute powerhouse! The snapdragon 8 gen 3 processor makes everything lightinhg fast-whether I'm gaming,multitasking , or editing photos. The 5000 mAh battery eaily lasts a full day even with heavy use, and the 45W fast charging ia a lifesaver.

    The S-pen integration is a great touch for note-taking and quick sketches, though I don't use it often. what really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

    However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's one UI still comes with bloatware-why do I need five different samsung apps for things google already provides? The $1300 price tage is also a hard pill to swallow: 

    pros: 
        insanely powerful processor(great for gaming and productivity)
        stunning 200MP camera with increadible zoom capabilities
        long battery life with fast charging
        S-Pen support is unique and useful
    
    Cons: 
        Bulky and heavy-not great for one-handed use
        Bloatware still exists in One UI
        Expensive compared to competitors
""")



print(result)
print(result['sentiment'])



# with_structured_output only works on: 
#     OpenAI GPT-4o
# GPT-3.5-turbo
# Claude
# Gemini (tool-enabled)
# use json for other models