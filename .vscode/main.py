import os
import rotas
from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para cadastrar uma pessoa
@app.route("/pessoas", methods = ["POST"])
def cadastro():
    result = rotas.cadastrar_pessoa(request)
    return jsonify(result)

# Rota para listar todas as pessoas cadastradas
@app.route("/pessoas", methods = ["GET"])
def listagem():
    if not os.path.exists('dados_pessoas.txt'):
        return jsonify({"message": "Arquivo de dados não existe."})
    
    result = rotas.listar_pessoas()
    return jsonify(result)

# Rota para buscar uma pessoa pelo CPF
@app.route("/pessoas/<string:cpf>", methods = ["GET"])
def busca(cpf):
    if not os.path.exists('dados_pessoas.txt'):
        return jsonify({"message": "Arquivo de dados não existe."})

    result = rotas.buscar_pessoa(cpf)
    return jsonify(result)

# Rota para atualizar uma pessoa pelo CPF
@app.route("/pessoas/<string:cpf>", methods = ["PUT"])
def atualizacao(cpf):
    if not os.path.exists('dados_pessoas.txt'):
        return jsonify({"message": "Arquivo de dados não existe."})
    
    result = rotas.atualizar_pessoa(cpf)
    return jsonify(result)

# Rota para remover uma pessoa pelo CPF
@app.route("/pessoas/<string:cpf>", methods = ["DELETE"])
def remocao(cpf):
    if not os.path.exists('dados_pessoas.txt'):
        return jsonify({"message": "Arquivo de dados não existe."})
    
    result = rotas.excluir_pessoa(cpf)
    return jsonify(result)

if __name__ == "__main__":
    app.run()