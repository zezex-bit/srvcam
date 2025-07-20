# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 12:03:36 2025

@author: José Malhó
"""

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

@app.post("/webhook/deliverybox")
async def receive_webhook(request: Request):
    data = await request.json()
    print("Received webhook:", data)
    return {"status": "ok"}
