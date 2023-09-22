# API_com_Python

O projeto em questão se trata de uma API simples para gerenciamento de funcionários em uma empresa. Esta API permite a realização de diversas operações, incluindo cadastro, listagem, busca, atualização e remoção de pessoas registradas no sistema. Para testar e utilizar essas funcionalidades de forma eficiente, é recomendado o uso da plataforma Postman. O Postman permite criar, salvar e enviar solicitações HTTP e HTTPs, além de facilitar a leitura das respostas recebidas.
Siga as instruções abaixo para executar cada uma das operações:

Cadastro:
1.	Adicione o seguinte URL: http://127.0.0.1:5000/pessoas
2.	Selecione o método HTTP POST.
3.	Na aba "Body", escolha a opção "raw" e defina o formato de texto como "JSON".
4.	No espaço de texto disponível, insira as informações da nova pessoa no seguinte formato:
{
    "nome": "Rafaela Ferreira Lovatti",
    "data_nascimento": "26-06-2004",
    "endereco": "Rua Itaú, 82",
    "cpf": "01234567890",
    "estado_civil": "Solteira"
}

OBS: Para realizar o cadastro, é importante seguir essas limitações:
•	Nome: esse campo deve conter no máximo 80 caracteres.
•	Data de nascimento: a data deve ser inserida no formato "DD-MM-YYYY" (dia-mês-ano)
•	Endereço: esse campo deve conter no máximo 80 caracteres. 
•	CPF: o CPF deve ter exatamente 11 dígitos numéricos, sem espaços ou caracteres especiais. 
•	Estado civil: esse campo deve ser preenchido com um dos seguintes valores: “Solteiro”, “Solteira”, “Casado”, “Casada”, “Divorciado”, “Divorciada”, “Viúvo” ou “Viúva”, que são os estados civis válidos, de acordo com a lei brasileira.

5.	Clique em "Send" para concluir a operação de cadastro.

Listagem:
1.	Adicione o seguinte URL: http://127.0.0.1:5000/pessoas
2.	Selecione o método HTTP GET.
3.	Clique em "Send" para listar todas as pessoas cadastradas.

Busca:
1.	A busca deve ser realizada com base no CPF, que é um atributo único para cada pessoa cadastrada.
2.	Adicione o URL http://127.0.0.1:5000/pessoas/ seguido do CPF desejado. 
Por exemplo: http://127.0.0.1:5000/pessoas/01234567890
3.	Selecione o método HTTP GET.
4.	Clique em "Send" para buscar uma pessoa pelo CPF especificado.

Atualização:
1.	Adicione o URL http://127.0.0.1:5000/pessoas/ seguido do CPF da pessoa a ser atualizada. 
Por exemplo: http://127.0.0.1:5000/pessoas/01234567890
2.	Selecione o método HTTP PUT.
3.	No espaço de texto disponível, atualize as informações da pessoa no seguinte formato:
{
    "nome": "Rafaela Ferreira Lovatti",
    "data_nascimento": "26-06-2004",
    "endereco": "Rua Itaú, 82",
    "cpf": "01234567890",
    "estado_civil": "Casada"
}
* Nesse caso, foi alterado o estado civil da pessoa, atualizando-o para “Casada”.

4.	Clique em "Send" para finalizar a operação de atualização.

Remoção:
1.	Adicione o URL http://127.0.0.1:5000/pessoas/ seguido do CPF da pessoa a ser removida. 
2.	Por exemplo: http://127.0.0.1:5000/pessoas/01234567890
3.	Selecione o método HTTP DELETE.
4.	Clique em "Send" para concluir a operação de remoção.

Para garantir que a interação com a API seja eficiente, é importante fornecer os dados corretos e usar os métodos HTTP apropriados para cada operação.
