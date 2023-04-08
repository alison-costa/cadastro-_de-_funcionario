class Cadastro:

    def __init__(self,name, cpf, idade, sexo, endereco):
        self.name = name
        self.__cpf = cpf
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def atendente(self):
        return 'Atendente'

@property
def cpf(self):
    return self.__cpf

@cpf.setter
def cpf(self, cpf):
    self.__cpf = cpf       