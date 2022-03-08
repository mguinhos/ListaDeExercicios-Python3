# https://wiki.python.org.br/EstruturaDeRepeticao
# Exercicio 3

'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''


from uteis import num

print('== PROGRAMA FAZER CADASTRO ==')

while nome := input("insira seu nome (minimo 3 letras): "):
    if len(nome) > 3:
        break
    else:
        print(nome, "não é um nome valido")

while idade := num(input("insira sua idade (entre 0 a 150): ")):
    if idade >= 0 and idade <= 150:
        break
    else:
        print(idade, 'não é uma idade valida')

while salario := num(input("insira seu salario (minimo 0): ")):
    if salario > 0:
        break
    else:
        print(salario, 'não é um salario valido')

while sexo := input('sexo (m/f): ').lower():
    if sexo == 'm' or sexo == 'f':
        break
    else:
        print(sexo, 'não é um sexo valido')

while estado_civil := input('estado civil (s; c; v; d): ').lower():
    if estado_civil in ('s', 'c', 'v', 'd'):
        break
    else:
        print(estado_civil, 'não é um estado civil válido')