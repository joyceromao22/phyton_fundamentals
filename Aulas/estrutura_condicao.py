# -*- coding: utf-8 -*-

# if, else

# idade = int(input('Digite sua idade: '))
# habilitacao = True

# if idade >= 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade')

# if idade >= 18 and habilitacao is True:
#     print('Você pode dirigir')

# else:
#     print('Você não pode dirigir')

# nota1 = int(input('Digite a primeira nota: '))
# nota2 = int(input('Digite a segunda nota: '))
# nota3 = int(input('Digite a terceira nota: '))
# nota4 = int(input('Digite a quarta nota: '))
# media = (nota1 + nota2 + nota3 + nota4) / 4
# if media >= 7: 
#     print('Você esta aprovado')

# else:
#     print('Você esta reprovado')


# Calculo de notas
# peça 4 notas do aluno
# se a nota final for maior que 7
# imprima aprovado
# se não
#imprima reprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1 + n2 + n3 + n4)/4

if media >= 7:
    print('Aluno aprovado')
elif media < 7 and media >= 5:
    print('Aluno em recuperação')
else:
    print('Aluno reprovado')