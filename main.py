# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 12:03:36 2025

@author: José Malhó
"""

from fastapi import FastAPI, Request

app = FastAPI()

# In-memory storage
matrix_a = []
matrix_b = []

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

# Webhook for Matrix A
@app.post("/webhook/a")
async def receive_matrix_a(request: Request):
    data = await request.json()
    print("📦 Matrix A Webhook received:", data)
    matrix_a.append(data)
    return {"status": "received by Matrix A"}

# Webhook for Matrix B
@app.post("/webhook/b")
async def receive_matrix_b(request: Request):
    data = await request.json()
    print("📦 Matrix B Webhook received:", data)
    matrix_b.append(data)
    return {"status": "received by Matrix B"}

# Endpoint to get Matrix A
@app.get("/data/a")
async def get_matrix_a():
    return matrix_a

# Endpoint to get Matrix B
@app.get("/data/b")
async def get_matrix_b():
    return matrix_b


############

#Receive Results

############

results_ab = []

@app.post("/webhook/ab/results")
async def receive_combined_results(request: Request):
    data = await request.json()
    print("🧮 Combined result received:", data)
    results_ab.append(data)
    return {"status": "ok"}

@app.get("/data/ab/results")
async def get_combined_results():
    return results_ab
