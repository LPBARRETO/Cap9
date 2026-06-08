from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# O FastAPI usa classes para validar se o JSON enviado está no formato correto
class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool = False

# Nossa base de dados simulada
tarefas = [
    {"id": 1, "titulo": "Aprender FastAPI", "concluida": False},
    {"id": 2, "titulo": "Dominar o Uvicorn", "concluida": False}
]

# Método GET
@app.get("/tarefas")
async def obter_tarefas():
    return tarefas

# Método POST (Note que usamos o status_code direto no decorador)
@app.post("/tarefas", status_code=201)
async def criar_tarefa(tarefa: Tarefa):
    # Converte o objeto recebido para um dicionário padrão do Python
    nova_tarefa = tarefa.model_dump()
    tarefas.append(nova_tarefa)
    return {"mensagem": "Tarefa criada com sucesso!", "tarefa": nova_tarefa}