from cadastro import Cadastro
from funcionario import Funcionario
from random import randint

nome = input('Digite um NOME: \n')
cpf = int(input('Digite um CPF: \n'))
idade = int(input('Digite uma IDADE: \n'))
sexo = input('Digite o SEXO: \n')
endereco = input('Digite um ENDERECO: \n')

codigo = randint (0000,9999)

cadastro = Cadastro(nome, cpf, idade, sexo, endereco)
print(f'Codigo do Funcionario: {codigo}')