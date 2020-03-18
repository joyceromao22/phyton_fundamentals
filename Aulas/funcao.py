# -*- coding: utf-8 -*-

# produtos = []

# def cadastrar_produto (produto):
#     global produtos
#     produtos.append(produto)

# def listar_produtos():
#     global produtos
#     for p in produtos:
#         print (p)

# def deleta_produto(produto):
#     global produtos
#     produtos.remove(produto)


# cadastrar_produto('abacaxi')
# cadastrar_produto('morango')
# cadastrar_produto('uva')


# deleta_produto('abacaxi')


# listar_produtos()

# def nome(seu_nome='Renato'):
#     print(seu_nome)

# nome('joyce')

# def adiciona_frutas(*itens):
#     global frutas
#     return frutas.append(itens)

# adiciona_frutas('abacaxi','limao','pera','uva')

# print(frutas)


# soma= lambda x,y:x+y

# print(soma(10,20))

#numeros = [1,2,3,4,5,6,7,8,9]

# dobro = list(map(lambda x: x *2,numeros))

# print(dobro)

# for x in numeros:
#     dobro = []
#     dobro.append(x*2)

# print(dobro)

#soma todos os numeros da lista em pares:
# from functools import reduce

# soma = reduce(lambda x, y: x+ y, numeros)

# print(soma)

#retorna apena snumeros pares:

#n_par = list(filter(lambda x: x % 2 == 0, numeros))
#print(n_par)

personagens = []

def addPersonagens(nomePersonagem):
    #global personagens
    personagens.append(nomePersonagem)

def rmvPersonagem(nomePersonagem):
    try:
        personagens.remove(nomePersonagem)
        print(f'Personagem:{nomePersonagem} removido!')
    except ValueError:
        print('Personagem nao cadastrado')


addPersonagens('Jerry')
rmvPersonagem('Jerry')

print(personagens