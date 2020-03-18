#importa banco postgree

# import psycopg2

# def insere_dados():
#     nome = input('digite o nome do projeto:')
#     conteudo = input('Digite o conteudo:')

#     try:
#         conexao = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")

#         cursor = conexao.cursor()

#         cursor.execute(f"insert into scripts(nome,conteudo) values('{nome}','{conteudo}')")
#         conexao.commit()
#         cursor.execute("Select * From scripts")
#         print(cursor.fetchall())
#         print('Registro criado com sucesso')


#     except Exception as e:
#         print(e)
#         print('Fazendo rollback')
#         conexao.rollback()
#     finally:
#         print("Finalizando conexao com o banco de dados")
#         cursor.close()
#         conexao.close()

# insere_dados()


#importa banco mysql

# import MySQLdb

# try:

#     con = MySQLdb.connect(host='localhost',user='admin',passwd='4linux',db='projetos')
#     cur = con.cursor()
#     cur.execute("insert into clientes(nome,endereco) values('Ana','Rua Vergueiro')")
#     con.commit()
#     print('Registro criado com sucesso')
# except Exception  as e:
#     print(f'Erro:{e}')
#     print('Fazendo rollback')
#     con.rollback()
# finally:
#     print('Finalizando conexao com o banco de dados')
#     cur.close()
#     con.close()

#banco mongodb

from pymongo import MongoClient

client = MongoClient('localhost')
db = client['dexterops']

def inserir_dados():
    try:
        db.fila.insert({"_id":15, "empresa": "4linux",
                        "cursos": [{"nome": "Continuos monitoring",
                                    "carga horaria": 40},
                                    {"nome": "Infraagil",
                                    "carga horaria":40}]})
    
    except Exception as e:
        print(f'Erro: {e}')
        db.fila.remove({"_id": 15})

# dado = {"_id":15, "empresa": "4linux",
#                         "cursos": [{"nome": "Continuos monitoring",
#                                     "carga horaria": 40},
#                                     {"nome": "Infraagil",
#                                     "carga horaria":40}]}

# print(dado['carga horaria'])


def buscar_dados():
    for r in db.fila.find():
        print(f"Empresa: {r['empresa']}")
        for c in r['cursos']:
            print('================')
            print(f"Nome: {c['nome']} \nCarga Horaria: {c['carga horaria']}")


def remove_dados():
    id = int(input('Digite o id: '))
    try:
        db.fila.remove({"_id":id})
    except Exception as e:
        print(f'Erro: {e}')
