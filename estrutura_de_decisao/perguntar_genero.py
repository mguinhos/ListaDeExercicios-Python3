# https://wiki.python.org.br/EstruturaDeDecisao
# Exercicio 3

'''
Autor: Marcel Guinhos
Disciplina: Laboratório de Programação - N01
'''


print('== PROGRAMA PERGUNTAR GENERO ==')

print('M: MASCULINO')
print('F: FEMININO')

generos = {
    "M": "Masculino",
    "F": "Feminino"
}

genero = input('insira seu genero: ').upper()

if genero_ := generos.get(genero):
    print('seu genero é', genero_)
else:
    print(genero, 'é um genero invalido')