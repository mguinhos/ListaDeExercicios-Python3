# https://wiki.python.org.br/EstruturaDeDecisao
# Exercicio 2

'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''


from uteis import num

print('== PROGRAMA NEGATIVO OU POSITIVO ==')

numero = num(input('insira um número: '))

if numero < 0:
    print('o número', numero, 'é negativo')
else:
    print('o número', numero, 'é positivo')