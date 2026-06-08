from flask import Flask

app = Flask(__name__)

# Rota principal (Hello World)
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Roda o servidor localmente na porta 5000
    app.run(debug=True)