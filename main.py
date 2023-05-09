from typing import Union
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from models import FormData, PromptRoadmap
from helpers import generate_ideas, generate_roadmap


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

@app.post("/initialize_form/")
async def submit_form(form_data: FormData):
    """
    Generate ideas for the user based on the form data

    Args:
        form_data (FormData): takes in the form data from the frontend

    Returns:
        ideas (dict): ideas generated for the user
    """
    try:
        link, email, name, role  = form_data.url, form_data.email, form_data.name, form_data.role
        ideas = generate_ideas(link)
        return {"ideas": ideas}
    except Exception as e:
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