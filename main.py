import json
from typing import Union
from starlette.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI
from models import PromptRoadmap, WebsiteDataPrompt, IdeasPrompt, SummaryPrompt
from helpers import generate_ideas, generate_roadmap, scrape_website, summarize_description


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"] 
)

@app.get("/")
def read_root():
    return {"Hello": "I'm TribeGPT"}

@app.post("/get_ideas/")
async def submit_form(body:IdeasPrompt):
    """
    Generate ideas for the user based on the form data

    Args:
        form_data (FormData): takes in the form data from the frontend

    Returns:
        ideas (dict): ideas generated for the user
    """
    try:
        ideas = generate_ideas(summary=body.summary, role=body.role)
        return json.loads(ideas)
    except Exception as e:
        print (e)
        return {"error": str(e)}

# Endpoint to generate a roadmap given an idea
@app.post("/generate_roadmap/")
async def gen_roadmap(body: PromptRoadmap):
    """
    Generate a roadmap for the (one) idea selected by the user

    Args:
        body (PromptRoadmap): takes in the idea selected by the user

    Returns:
        roadmap (dict): roadmap for the idea
    """
    try:
        selected_idea = body.idea_prompt
        roadmap = generate_roadmap(selected_idea)
        return {"roadmap": roadmap}
    
    except Exception as e:
        return {"error": str(e)}

# Endpoint to retrieve text describing the website
@app.post("/website_data/")
async def gen_website_data(body: WebsiteDataPrompt):
    """
    """
    try:
        website__data = scrape_website(body.url)
        return website__data
    
    except Exception as e:
        return {"error": str(e)}

# Endpoint to retrieve text describing the website
@app.post("/summarize/")
async def gen_summary(body: SummaryPrompt):
    """
    """
    try:
        website__data = summarize_description(body.description)
        return website__data
    
    except Exception as e:
        return {"error": str(e)}


@app.get("/ping")
async def gen_ping():
    return {"status": "ok"}
