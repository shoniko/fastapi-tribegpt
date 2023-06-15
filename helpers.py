
import openai
from llama_index import  download_loader
from urllib.parse import urlparse
from dotenv import load_dotenv
import os 
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")
bsl_loader = BeautifulSoupWebReader()

MAX_PROMPT_SIZE = 8000

def chat_openai(prompt, system_text="",token_limit=2048):
    """ construct an openai gpt3.5/gpt4 call

    Args:
        prompt (str): input_prompt
        system_text (str, optional): system text. Defaults to "".
        token_limit (int, optional): token limit for the api call. Defaults to 2048.

    Returns:
        output (str):  output text
    """
    chat_query = [{"role":"system", "content": system_text}, {"role":"user", "content": prompt}]

    response = openai.ChatCompletion.create(
            messages=chat_query,    
            model="gpt-4-0314",
            # model = "gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=token_limit
            )
    output = response["choices"][0]["message"]["content"]
    return output

def scrape_website(web_url:str):
    """
    Scrape the website for the company description

    Args:
        web_url (str): URL of the website

    Returns:
        str: Company description/summary
    """

    # BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")
    
    documents = bsl_loader.load_data(urls=[web_url])
    text_description = documents[0].text

    print(text_description)
    return text_description

def get_ideas(text_description:str, role:str):
    summarize_prompt = f'''
                  Lets think step by step to get the best machine learning and artificial intelligence business ideas possible.
            
            Website Context:
            {text_description[:3000]}

           Role: {role}'''.format(role=role)

    system_text = """
                        -You are Steve, an A.I. and Machine Learning Solutions Architect. You are tasked with taking the given inputs ["web_Context","Role"] from a business owner, and providing them with an output ["3 great ideas for how artificial intelligence or machine learning can improve their business" ].

-Each idea should have a minimum word count of 400.
-Follow these steps in constructing your ideas: 
1)Choose a title that would appeal to someone in the given role at that business.
Make your proposals as practical and relevant as possible to the business's needs and goals.
2)Begin with a sentence that explains how ML and/or A.I. will be used in the idea proposed in the title,
relate it to the user's "role".
3)Write another sentence that further explains how this idea/product will be helpful to someone in the user's "role"
and for the specific business(found in the web_context) they serve in this role for.


-Format

 Return in json. 3_Business_Ideas should be structured this way ''' {
                        "idea_1_title": "",
                "idea_1_discription":"",
                        "idea_2_title":  "",
                "idea_2_discription":"",,
                        "idea_3_title":  "",
                "idea_3_discription":"",
            
 Begin your response with:
' { "idea_1_title" '

-Remember, you're an excellent solutions architect and you will use your expertise and background knowledge to provide the best possible business ideas. 
         
    """

    print(system_text)
    print(summarize_prompt)

    chat_query = [{"role":"system", "content": system_text}, {"role":"user", "content": summarize_prompt}]
    
    web_summary = openai.ChatCompletion.create(
            messages=chat_query,    
            model="gpt-4-0314",
            #model = "gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=2000
            )
    print("ideas done")
    web_summary = web_summary["choices"][0]["message"]["content"]
    print("-------------------")
    print(web_summary)
    return web_summary
