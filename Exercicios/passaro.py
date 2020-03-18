class Passaro():
    def __init__(self):
        self.penas = True
        self.asas = 2
        self.bico = True
        self.patas = 2
        self.rabo = True
        self.olhos = 2

    def voar(self):
        print('Passaro voando')
    
    def pousar(self):
        print('Pousando')

    def dormir(self):
        print('Dormindo')

    def comer(self):
        print('comendo')


class Sabia(Passaro):

    def cantar(self):
        print('cantando')


class galinha(Passaro):
    def voar(self):
        print('galinha nao voa')
    def pousar(self):
        print('galinha nao pousa') 

p1 = Sabia()
p2 = galinha()

p2.voar()



# Faça uma classe sabia que herde caracteristicas do Passaro
# e as use
# Faça uma galinha que herde caracteristicas de Passo
# e mantenha as suas