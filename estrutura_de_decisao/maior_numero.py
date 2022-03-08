# https://wiki.python.org.br/EstruturaDeDecisao
# Exercicio 1

'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''


from uteis import num

print('== PROGRAMA MAIOR NUMERO ==')

primeiro_numero = num(input('insira o primeiro numero: '))
segundo_numero = num(input('insira o segundo numero: '))

if primeiro_numero > segundo_numero:
    print(primeiro_numero, 'é maior que', segundo_numero)
elif primeiro_numero == segundo_numero:
    print(primeiro_numero, 'é igual a', segundo_numero)
else:
    print(segundo_numero, 'é maior que', primeiro_numero)