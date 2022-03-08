# https://wiki.python.org.br/EstruturaSequencial
# Exercicio 4

'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''


from uteis import num

print('== PROGRAMA PEDIR NÚMERO ==')

nota_a = num(input('insira a nota do primeiro bimeste: '))
nota_b = num(input('insira a nota do segundo bimestr: '))
nota_c = num(input('insira a nota do terceiro bimeste: '))
nota_d = num(input('insira a nota do quarto bimeste: '))

media = (nota_a + nota_b + nota_c + nota_d) / 4

print('a média simples do aluno é', media)