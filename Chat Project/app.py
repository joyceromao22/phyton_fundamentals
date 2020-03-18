import Modules.Banco as banco
import threading

if __name__== "__main__":
    db = banco.BancoDados()
    user = input('Digite o seu usuario:')
    try:
        f = threading.Thread(target=db.visualizar)
        f.start()
    except Exception as e:
        print(f'Falha ao criar thread: {e}')
    while f.is_alive:
        mensagem = input('> ')
        db.cadastrar(user,mensagem)



