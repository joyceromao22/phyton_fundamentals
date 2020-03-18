from sqlalchemy import update
from core import user_table,engine


conexao = engine.connect()

nome_antigo = input('digite o antigo nome:')
novo_nome = input('digite o novo nome: ')

atualizar = update(user_table).where(user_table.c.nome == nome_antigo)

atualizar = atualizar.values(nome=novo_nome)
resultado = conexao.execute(atualizar)
print(resultado.rowcount)