# -*- coding: utf-8 -*-

vlr_hora = float(input('Digite o valor da hora: '))
qtd = float(input('Digite q quantidade de horas trabalhadas'))

salariobruto = (vlr_hora * qtd)

if salariobruto >= 4600:
    IR = 27
elif salariobruto > 3700 and salariobruto <4600:
    IR = 22
elif salariobruto > 2800 and salariobruto <= 3700:
    IR = 15
elif salariobruto > 1900 and salariobruto<=2800:
    IR = 7
else:
    IR = 0

valorIR= salariobruto * (IR/100.0)
valorSindicato = salariobruto * (3 / 100.0)
valorFGTS = salariobruto * (11 / 100.0)

salarioliquido = salariobruto -  (valorIR + valorSindicato)

print(f'Valor do salario bruto:( {vlr_hora} * {qtd}) : R$ {salariobruto}')
print(f'(-) IR({IR}%):R$ {valorIR}')
print(f'(-) Sindicato (3%): R$ {valorSindicato}')
print(f'FGTS (11%):R$ {valorFGTS}')
print(f'Total de Descontos : R$ {valorIR + valorSindicato}')
print(f'Slario Liquido: R$ {salarioliquido}')

