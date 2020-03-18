# -*- coding: utf-8 -*-

#erros e excessoes

# while True:
#     try:
#         x = int(input('Digite o primeiro numero: '))
#         y = int(input('Digite o segundo numero: '))
#         print(f'resultado: {x +y}')
#     except Exception as e:
#         print('Digite apenas numeros!')

funcionarios = ['rafael', 'mariana', 'paulo']

try:
    f = input('nome: ')
    if f in funcionarios:
        print('voce e um funcionario')
    else:
        raise NameError, ('voce e um funcionario')
except NameError as n:
    print (n)