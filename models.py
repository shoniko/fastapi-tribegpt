from fastapi import FastAPI, Form
from pydantic import BaseModel, validator, constr

app = FastAPI()

class FormData(BaseModel):
    url: constr(strip_whitespace=True, to_lower=True) = None
    email: str = ""
    name: str = ""
    company_role: str = ""

    @validator('url')
    def validate_url(cls, url):
        print(url)
        if url is not None and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        #     raise ValueError('URL must start with http:// or https://')
        return url

    @validator('email')
    def validate_email(cls, email):
        if email is not None and email.endswith('@example.com'):
            raise ValueError('Email cannot be a example.com email address')
        return email
    
    @classmethod
    def as_form(
        cls,
        url: str = Form(0),
        email: str = Form(1),
        name: str = Form(2),
        company_role: str = Form(3)
    ):
        return cls(url=url, email=email, name=name, company_role=company_role)


class PromptRoadmap(BaseModel):
    idea_prompt: str

class WebsiteDataPrompt(BaseModel):
    url: str
    @validator('url')
    def validate_url(cls, url):
        print(url)
        if url is not None and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        #     raise ValueError('URL must start with http:// or https://')
        return url

class IdeasPrompt(BaseModel):
    summary: str
    role: str

class SummaryPrompt(BaseModel):
    description: str
