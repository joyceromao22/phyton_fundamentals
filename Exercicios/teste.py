# """
# Crie uma classe Carro
# ela deve ter os atributos:
#    * 4 rodas
#    * portas
#    * motor
#    * vidros
#  e os seguint métodos:
#    * ligar
#    * acelerar
#    * frear
#    * desligar
# """

class Carro():

    def __init__(self):
        self.motor = True
        self.rodas = 4
        self.vidros = True
        self.portas = 4
        self.ligado = False
        
    def ligar(self):
        if self.ligado == False:
            print('Ligando...')
            print('ligado!')
            self.ligado = True
        else:
            pass

    def acelerar(self):
        if self.ligado == True:
            print('Acelerando...')
            self.parado = False
        else:
            self.parado = True

    def frear(self):
        if self.parado == False:
            print('Freando...')
        else:
            pass

    def desligar(self):
        if self.ligado == True:
            print('Desligando carro')
            self.ligado = False
        else:
            pass

fox = Carro()
fox.ligar()
fox.acelerar()
fox.frear()
fox.desligar()
fox.acelerar()

import POO_EX

p3 = POO_EX.Passaro()