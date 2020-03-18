class Carro():
    def __init__(self):
        self.rodas = 4
        self.portas = 4
        self.motor =  True
        self.vidros = True
        self.ligado = False
        


    def ligar(self):
        if self.ligado == False:
            print('carro ligado')
            self.ligado = True
        else:
            pass

    def acelerar(self):
        if self.ligado == True:
            print('carro acelerado')
            self.parado = False
        else:
            self.parado =  True

    def frear(self):
        if self.parado == False:
            print ('Freando')
        else:
            pass

    def desligar(self):
        if self.ligado == True:
            print('carro desligado')
            self.ligado = False       
        else:
            pass

fox = Carro()

fox.ligar()
fox.acelerar()
fox.frear()
fox.desligar()
fox.acelerar()