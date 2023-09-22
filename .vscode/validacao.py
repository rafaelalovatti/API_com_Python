from marshmallow import Schema, ValidationError, fields

def verifica_cpf(cpf):
    """
    Verifica se o cpf está no formato 12345678900
    """
    if len(cpf) == 0:
        raise ValidationError("Este campo não deve estar vazio.")
    
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValidationError("CPF inválido.")

def verifica_estado_civil(estado_civil):
    """
    Verifica se o estado civil é válido de acordo com a legislação
    """
    estados_civis = ['Solteiro', 'Solteira', 'Casado', 'Casada', 'Divorciado', 'Divorciada', 'Viúvo', 'Viúva']

    if len(estado_civil) == 0:
        raise ValidationError("Este campo não deve estar vazio.")

    if estado_civil.title() not in estados_civis:
        raise ValidationError("Estado civil inválido.")

def verifica_data(data_nascimento):
    """
    Verifica se está no formato DD-MM-YYYY e se os valores digitados 
    para dia, mês e ano são válidos
    """
    if len(data_nascimento) == 0:
        raise ValidationError("Este campo não pode estar vazio.")
    if len(data_nascimento) != 10:
        raise ValidationError("Data inválida. Use o formato DD-MM-YYYY.")
    
    for i in range(10):
        if i == 2 or i == 5:
            if data_nascimento[i] != "-":
                raise ValidationError("Data inválida. Use o formato DD-MM-YYYY.")
        else:
            if not data_nascimento[i].isdigit():
                raise ValidationError("Data inválida. Use apenas algarismos no formato DD-MM-YYYY.")

    dia, mes, ano = map(int, data_nascimento.split('-'))
    
    if not 1923 <= ano <= 2023 or not 1 <= mes <= 12 or not 1 <= dia <= 31:
        raise ValidationError("Data inválida. Verifique os valores digitados.")
    
def verifica_nome_endereco(string):
    """
    Verifica se as strings do nome e do endereço não ultrapassam 80 caracteres cada
    """
    if len(string) == 0:
        raise ValidationError("Este campo não pode estar vazio.")
    
    if len(string) > 80:
        raise ValidationError("Número máximo de 80 caracteres excedido.")
   
class PessoaSchema(Schema):
    """
    Schema para validação de dados da pessoa
    """
    nome = fields.String(validate = verifica_nome_endereco)
    data_nascimento = fields.String(validate = verifica_data)
    endereco = fields.String(validate = verifica_nome_endereco)
    cpf = fields.String(validate = verifica_cpf)
    estado_civil = fields.String(validate = verifica_estado_civil)