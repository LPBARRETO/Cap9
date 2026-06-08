from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Aprender Flask", "concluida": False},
    {"id": 2, "titulo": "Fazer os exercícios do Capítulo 9", "concluida": False}
]

@app.route('/tarefas', methods=['GET'])
def obter_tarefas():
    return jsonify(tarefas), 200

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    nova_tarefa = request.get_json()
    tarefas.append(nova_tarefa)
    return jsonify({"mensagem": "Tarefa criada!", "tarefa": nova_tarefa}), 201

if __name__ == '__main__':
    # Roda na porta 5001 para não dar conflito com o Hello World
    app.run(port=5001, debug=True)