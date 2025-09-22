from fastapi import FastAPI 

app = FastAPI()

@app.get("/") #Suporta requisições demoradas (banco de dados)
async def root():
    return {"message": "Hello World"}