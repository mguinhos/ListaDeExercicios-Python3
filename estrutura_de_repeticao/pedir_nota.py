# https://wiki.python.org.br/EstruturaDeRepeticao
# Exercicio 1

'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''


from uteis import num

print('== PROGRAMA PEDIR NOTA ==')

while nota := num(input("dê uma nota de 0 a 10: ")):
    if nota >= 0 and nota <= 10:
        break
    else:
        print(nota, 'não é uma nota valida!')

print('a nota que você deu foi', nota)