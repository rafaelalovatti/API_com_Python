import os
import json
from flask import request
from validacao import PessoaSchema

def buscar_pessoa(cpf):
    """
    Busca uma pessoa a partir do seu CPF no arquivo de dados
    """
    pessoa_buscada = None
    with open('dados_pessoas.txt', 'r') as file:
        for line in file:
            pessoa_dados = json.loads(line) # Carrega os dados em JSON para Python
            if pessoa_dados['cpf'] == cpf:
                pessoa_buscada = pessoa_dados
                break

    if pessoa_buscada is not None:
        pessoa_dados = {
            "nome": pessoa_buscada['nome'].title(),
            "data_nascimento": pessoa_buscada['data_nascimento'],
            "endereco": pessoa_buscada['endereco'].title(),
            "cpf": pessoa_buscada['cpf'],
            "estado_civil": pessoa_buscada['estado_civil'].title()
        }
        return pessoa_dados
    
    return f"Pessoa com CPF {cpf} não encontrada"


def cadastrar_pessoa(request):
    """
    Cadastra/adiciona uma nova pessoa no arquivo de dados
    """
    pessoa_schema = PessoaSchema()
    
    dados = request.get_json()

    # Valida os dados usando o schema 
    errors = pessoa_schema.validate(dados)
    if errors:
        return errors

    cpf = dados['cpf']
    
    # Verifica se o arquivo já existe
    if not os.path.isfile('dados_pessoas.txt'):
        with open('dados_pessoas.txt', 'w'):
            pass  # Cria um arquivo vazio
    
    # Verifica se já existe uma pessoa com o mesmo CPF
    with open('dados_pessoas.txt', 'r') as file:
        for line in file:
            pessoa_dados = json.loads(line)
            if pessoa_dados['cpf'] == cpf:
                return "CPF já cadastrado."

    # Salva os dados no arquivo
    with open('dados_pessoas.txt', 'a') as file:
        file.write(json.dumps(dados) + '\n')

    return "Pessoa cadastrada com sucesso"

def listar_pessoas():
    """
    Retorna todas as pessoas presentes no arquivo de dados
    """
    pessoas_dados = []
    
    # Lê todas as pessoas do arquivo de dados
    with open('dados_pessoas.txt', 'r') as arquivo:
        for linha in arquivo:
            pessoa_dados = json.loads(linha)
            pessoa_dados = {
                "nome": pessoa_dados['nome'].title(),
                "data_nascimento": pessoa_dados['data_nascimento'],
                "endereco": pessoa_dados['endereco'].title(),
                "cpf": pessoa_dados['cpf'],
                "estado_civil": pessoa_dados['estado_civil'].title()
            }
            pessoas_dados.append(pessoa_dados)

    # Ordena a lista de pessoas por CPF
    pessoas_dados.sort(key = lambda pessoa: pessoa['cpf'])
    
    return pessoas_dados

def excluir_pessoa(cpf):
    """
    Remove uma pessoa do arquivo de dados, a partir de uma 
    prévia busca por seu CPF
    """
    pessoas_atualizadas = []
    pessoa_excluida = False

    # Lê todas as pessoas do arquivo de dados e procura pela pessoa com o CPF fornecido
    with open('dados_pessoas.txt', 'r') as file:
        for line in file:
            pessoa_dados = json.loads(line)
            if pessoa_dados['cpf'] != cpf:
                pessoas_atualizadas.append(pessoa_dados)
            else:
                pessoa_excluida = True

    if pessoa_excluida:
        # Atualiza o arquivo de dados com as pessoas excluindo a encontrada
        with open('dados_pessoas.txt', 'w') as file:
            for pessoa_dados in pessoas_atualizadas:
                file.write(json.dumps(pessoa_dados) + '\n')
        return f"Pessoa com CPF {cpf} excluída"
    
    return f"Pessoa com CPF {cpf} não encontrada"

def atualizar_pessoa(cpf):
    """
    Atualiza os dados de uma pessoa no arquivo de dados, 
    a partir de uma prévia busca por seu CPF
    """
    pessoa_schema = PessoaSchema()
    dados = request.get_json()
    
    # Valida os dados usando o schema
    errors = pessoa_schema.validate(dados)
    if errors:
        return errors
    
    # Realiza a busca no arquivo de dados
    pessoa_atualizar = None
    pessoas_atualizadas = []

    with open('dados_pessoas.txt', 'r') as file:
        for line in file:
            pessoa_dados = json.loads(line)
            if pessoa_dados['cpf'] == cpf:
                pessoa_atualizar = pessoa_dados
                pessoa_dados.update(dados)  # Atualiza os campos existentes com os novos dados
            pessoas_atualizadas.append(pessoa_dados) # Adiciona as pessoas que já existiam e a pessoa atualizada

    if pessoa_atualizar is not None:
        # Reescreve o arquivo de dados com as pessoas atualizadas
        with open('dados_pessoas.txt', 'w') as file:
            for pessoa_dados in pessoas_atualizadas:
                file.write(json.dumps(pessoa_dados) + '\n')
        return f"Pessoa com CPF {cpf} atualizada"
    
    return f"Pessoa com CPF {cpf} não encontrada"