from flask import Flask

app = Flask("Livro de Receitas")

@app.route("/Livro_de_receitas", methods=["GET"])
def Livro_de_receitas():
    return {"Livro": "de receitas"}

@app.route("/cadastra/Receitas", methods=["POST"])
def cadastraReceitas():
    return {"Receita": 1}    
app.run()

#master
