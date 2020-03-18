class Cadastro():

def __init__(self, nome, cpf, rg):
    self.nome = nome
    self.cpf = cpf
    self.rg = rg
    
def verificaCPF(self):
    if len(self.cpf) == 11:
        return 'CPF OK'