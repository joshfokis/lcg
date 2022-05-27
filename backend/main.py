from telnetlib import SE
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configs.set_generator import SetGenerator

import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
     return {"message": "Hello World"}

@app.get('/arkham')
async def arkham():
    s = SetGenerator()
    s.response = requests.get("https://arkhamdb.com/api/public/cards/core").json()
    game = s.generate_config()
    print('got')
    return game