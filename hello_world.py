from flask import Flask

app = Flask(__name__)

# Rota principal (Hello World)
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Roda na porta 5000
    app.run(port=5000, debug=True)