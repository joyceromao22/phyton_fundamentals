# -*- coding: utf-8 -*-

# with open('primeiro_arquivo', 'w') as f:
#     f.write('Esse e um arquivo de texto simples')
#     f.close()


with open('primeiro arquivo' , 'w') as f:
    f.seek(0)
    f.write('curso de python')
    f.close()

with open ('primeiro_arquivo','r') as f:
    print(f.readlines())
    f.seek(0)