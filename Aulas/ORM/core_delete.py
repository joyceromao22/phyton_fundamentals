from sqlalchemy import delete
from core import user_table, engine

nome = input('Digite o nome:')

conexao = engine.connect()
apagar = delete(user_table).where(user_table.c.nome == nome)
resultado = conexao.execute(apagar)
print(f'quantidade de linhas afetadas: {resultado.rowcount}')