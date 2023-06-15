from random import shuffle


def palavra(s):
    lista = list(s)
    shuffle(lista)
    lista = ''.join(lista)
    print('->', lista)


while True:
    print('=' * 40)
    p = input('Digite algo para embaralhar: ')
    palavra(p)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=' * 40)
print('<<< Finalizado >>>')
