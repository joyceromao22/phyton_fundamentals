from core import user_table,engine

try:

    con = engine.connect()
    ins = user_table.insert()

    name = input('Digite o nome:')
    age = int(input('Digite a idade:'))
    password = input('Digite a senha:')

    novo_valor = ins.values(idade=age,nome=name,senha=password)
    con.execute(novo_valor)
    print(f'usuario {name} cadastraddo com sucesso')

except Exception as e:
    print(f'Erro:{e}')