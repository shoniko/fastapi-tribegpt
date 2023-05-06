from fastapi import FastAPI, Form
from pydantic import BaseModel, validator, constr

app = FastAPI()

class FormData(BaseModel):
    url: constr(strip_whitespace=True, to_lower=True) = None
    email: str = None
    name: str = None
    role: str = None

    @validator('url')
    def validate_url(cls, url):
        if url is not None and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        #     raise ValueError('URL must start with http:// or https://')
        return url

    @validator('email')
    def validate_email(cls, email):
        if email is not None and email.endswith('@example.com'):
            raise ValueError('Email cannot be a example.com email address')
        return email


class PromptRoadmap(BaseModel):
    prompt: str
