from pymongo import MongoClient, DESCENDING
import time
class BancoDados():

    def __init__(self):
        try:
           client = MongoClient('192.168.205.89')
           self.db = client['chat']

        except Exception as e:
            print(e)
            exit()


    def cadastrar(self,nome,mensagem):
        data = {'nome':nome,
                'mensagem':mensagem,
                'hora': time.strftime('%d-%m-%Y %H:%M:%S')}
        self.db.chat.insert(data)

    def visualizar(self):
        ultimoRegistro = [rg for rg in self.db.chat.find().sort("_id",DESCENDING)]
        while True:
            data = [rg for rg in self.db.chat.find().sort("_id",DESCENDING)]
            if data != ultimoRegistro:
                ultimoRegistro = data
                dado = ultimoRegistro[0]
                print("[{}] {} : {}".format(dado['hora'],dado['nome'],dado['mensagem']))
                time.sleep(2)
