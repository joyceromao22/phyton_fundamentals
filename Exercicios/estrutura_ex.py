# dado a lista

times = ['time', ['Corinthians', 'Palmeiras', 'São Paulo'], 'cores', ['Preto', 'Branco', 'Verde', 'Vermelho']]

# imprima na tela as seguintes mensagens:


# time: <nome_time>, cores: <cores_time> 

#time: Corinthians, cores: Preto, Branco

print(f'{times[0]}: {times[1][0]}, {times[2]}: {times[3][0]}, {times[3][1]}')
print(f'{times[0]}: {times[1][1]}, {times[2]}: {times[3][2]}, {times[3][1]}')
print(f'{times[0]}: {times[1][2]}, {times[2]}: {times[3][0]}, {times[3][1]}, {times[3][3]}')

