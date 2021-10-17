from flask import Flask
from werkzeug.datastructures import RequestCacheControl

app = Flask("Livro de Receitas")

@app.route("/livros", methods=["GET"])
def Livrodereceitas():
    return {"Livro": "de receitas"}

@app.route("/cadastro/Receitas", methods=["POST"])
def cadastroReceitas():
    body = Request.get_json()
    print(body)
    return body    
app.run()


