from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Processo(BaseModel):
    numero_cnj: str
    vara: str
    status: str
    valor_da_causa: str


processos = [
    {
        "numero_cnj": "0000001-11.2025.8.26.0001",
        "vara": "10ª Cível",
        "status": "ARQUIVADO",
        "valor_da_causa": "10000.00",
    },
    {
        "numero_cnj": "0000002-93.2025.8.26.0001",
        "vara": "10ª Cível",
        "status": "SUSPENSO",
        "valor_da_causa": "50000.00",
    },
    {
        "numero_cnj": "0000003-78.2025.8.26.0001",
        "vara": "10ª Cível",
        "status": "EM_ANDAMENTO",
        "valor_da_causa": "100000.00",
    },
]


@app.get("/")
def saudar():
    return {"mensagem": "API do SMJuris no ar", "versao": "0.1.0"}


@app.get("/processos")
def listar_processos():
    return processos


@app.get("/processos/{numero_cnj}")
def consultar_processo(numero_cnj: str):
    for processo in processos:
        if numero_cnj == processo["numero_cnj"]:
            return processo
    raise HTTPException(status_code=404, detail="Processo não encontrado.")


@app.post("/processos", status_code=201)
def cadastrar_processo(processo: Processo):
    for cadastrado in processos:
        if processo.numero_cnj == cadastrado["numero_cnj"]:
            raise HTTPException(status_code=409, detail="Processo já cadastrado.")
    processos.append(processo.model_dump())
    return processo
