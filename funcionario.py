from cadastro import Cadastro

class Funcionario(Cadastro):
    def numero_funcionario(self, nome, cpf, idade, sexo, endereco, codigo):
        super().__init__(nome, cpf, idade, sexo, endereco)
        self.codigo = codigo
    
    def atendente(self):
        return 'Gerenciador de processos !'