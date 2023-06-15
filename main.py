import json
from typing import Union
from starlette.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI
from models import WebsiteDataPrompt, IdeasPrompt
from helpers import scrape_website, get_ideas


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
@app.post("/get_ideas/")
async def gen_summary(body: IdeasPrompt):
    """
    """
    try:
        print("Calling summarize")
        ideas = get_ideas(body.description, body.role)
        return json.loads(ideas)
    
    except Exception as e:
        return {"error": str(e)}


@app.get("/ping")
async def gen_ping():
    return {"status": "ok"}
