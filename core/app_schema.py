from fastapi import FastAPI
from pydantic import BaseModel

class AppSchema(BaseModel):
    name: str
    description: str
    version: str    
    path: str
    router: FastAPI = None  # This will be set when the app is mounted