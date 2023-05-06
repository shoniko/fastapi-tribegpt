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
    return {"Hello": "World"}

@app.post("/initialize_form/")
async def submit_form(form_data: FormData):
    try:
        link, email, name, role  = form_data.url, form_data.email, form_data.name, form_data.role
        ideas = generate_ideas(link)
        return {"ideas": ideas}
    except Exception as e:
        return {"error": str(e)}

# Endpoint to generate a roadmap given an idea
@app.post("/process-prompt/")
async def process_prompt(prompt_input: PromptRoadmap):
    prompt = prompt_input.prompt
    # Do something with the prompt
    return {"prompt": prompt}
