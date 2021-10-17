from flask import Flask ,app , request
from flask.json import jsonify
import json

app = Flask(__name__)

receitas = [
    {
        "Título": "Bolo01",
        "Lista de ingredientes": [
            "ingrediente01"
            "ingrediente02"
            "ingrediente03"
        ],

        "modo": "modo01",
        "Redimento": "Redimento01"
        
    },
   
]

# @app.route("/cadastro1", methods=["GET"])
# def Cadastro1():
#    return receitas


@app.route("/cadastro", methods=["POST","GET"])
def Cadastro():
    if request.method == "GET":
        return jsonify(receitas)
    elif request.method == "POST":
        newcadastro = json.loads(request.data)
        receitas.append(newcadastro)
        return jsonify({
            "menssagem" : "Cadastrado",
            "newValue": newcadastro

        })
   
if __name__ == '__main__':
    app.run(debug=True)




