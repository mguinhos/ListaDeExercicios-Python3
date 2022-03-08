# https://wiki.python.org.br/EstruturaDeRepeticao
# Exercicio 7

'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''


from uteis import num

print('== PROGRAMA MAIOR NUMERO ==')

while numeros := tuple(map(num, input('insira cinco ou mais numeros (separados por espacos): ').split())):
    if len(numeros) >= 5:
        print('o maior numero é', max(numeros))
    else:
        print('você só inseriu', len(numeros), 'numeros')