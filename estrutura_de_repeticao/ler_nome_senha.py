# https://wiki.python.org.br/EstruturaDeRepeticao
# Exercicio 2

'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''


print('== PROGRAMA LER NOME E SENHA ==')

while True:
    nome_de_usuario = input("insira seu nome de usuario: ")
    senha_do_usuario = input("insira sua senha: ")

    if nome_de_usuario == senha_do_usuario:
        print("sua senha não deve ser igual ao nome de usuario!")
    else:
        break