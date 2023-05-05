from typing import Union
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from models import FormData, PromptRoadmap


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
    
    return form_data.dict()

# Endpoint to generate a roadmap given an idea
@app.post("/process-prompt/")
async def process_prompt(prompt_input: PromptRoadmap):
    prompt = prompt_input.prompt
    # Do something with the prompt
    return {"prompt": prompt}
