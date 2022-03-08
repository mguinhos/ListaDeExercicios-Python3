# https://wiki.python.org.br/EstruturaDeRepeticao
# Exercicio 6

'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''


print('== PROGRAMA NUMEROS UM A VINTE ==')

numeros_um_a_vinte = []

for numero in range(1, 21):
    numeros_um_a_vinte.append(numero)

for numero in numeros_um_a_vinte:
    print(numero)

print(*numeros_um_a_vinte)