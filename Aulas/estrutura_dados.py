#-*- coding: utf-8 -*-

#listas

# frutas = ['abacaxi', 'maca', 'limao']

# print(frutas)
# print(frutas [2]) #indexacao

#lista = [1, 1.5, 'estrela', False, ['a','b','c']]

#print (lista[4][1]) #imprime subitem da lista

#print (lista([-1]) #imprimi ultimo valor

# imutaveis = (1,2,3, ['a','b','c'], 'limao')
# print (imutaveis.count('limao'))

# dicionario = {'nome': 'Joyce','Sobrenome': 'Romao', 'idade': 29}
# print (dicionario ['idade'])

produtos = {'produtos': {'0001': {'nome': 'camiseta hulk',
                                  'valor': 79.9},
                         '0002': {'nome': 'camiseta star wars',
                                  'valor': 99.9}
                         }
            }

#print(produtos['produtos']['0001'].values())
print(produtos['produtos']['0001'].keys())
# print(produtos['produtos']['0001']['nome'])