from time import sleep


def reverso(n):
    if n.isnumeric():
        r = str(n[::-1])
        return print(f' {n} -> {r}')


print('=' * 40)
print(f'{"REVERSO DE UM NÚMERO":^40}')
while True:
    while True:
        print('=' * 40)
        num = str(input('Digite um número: '))
        sleep(0.5)
        reverso(num)
        if num.isnumeric():
            break
        else:
            print(f'Erro! Digite apenas números inteiros')
    print('=' * 40)
    resp = str(input('Deseja fazer novamente? [S/N] '))
    if resp in 'Nn':
        break
print('=' * 40)
print('  ENCERRANDO... ')
sleep(2)
print('-' * 40)
print('<<< Finalizado! >>>')
