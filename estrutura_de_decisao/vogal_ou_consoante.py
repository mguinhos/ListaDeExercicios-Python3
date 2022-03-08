# https://wiki.python.org.br/EstruturaDeDecisao
# Exercicio 44

print('== PROGRAMA VOGAL OU CONSOANTE ==')

letra = input('insira uma letra: ')

if letra in 'aeiou':
    print('a letra', letra, 'é uma vogal!')
else:
    print('a letra', letra, 'é uma consoante!')