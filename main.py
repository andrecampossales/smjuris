from fastapi import FastAPI, HTTPException

app = FastAPI()

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
