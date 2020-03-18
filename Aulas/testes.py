from unittest import Testcase,main


def somar(x,y):
    return x + y

def subtraiar(x,y):
    return x - y

def dividir(x,y):
    return x / y

def multiplicar(x,y):
    return x * y

class Testes(Testecase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(5,2),10)

