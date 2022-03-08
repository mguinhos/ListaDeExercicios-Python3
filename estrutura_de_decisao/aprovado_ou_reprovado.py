'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''

# https://wiki.python.org.br/EstruturaDeDecisao
# Exercicio 5

from uteis import num

print('== PROGRAMA APROVADO OU REPROVADO ==')

primeira_nota = num(input('insira a primeira nota: '))
segunda_nota = num(input('insira a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

if media >= 9.99:
    print('APROVADO!!!')
elif media >= 7.0:
    print('Aprovado!')
else:
    print('Reprovado!')