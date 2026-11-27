from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def saudacao():
    return {"mensagem": "API do SMJuris no ar", "versao": "0.1.0"}
