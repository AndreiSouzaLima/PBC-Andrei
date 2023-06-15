from time import sleep


def leiaint(n):
    if n.isnumeric():
        reverso = n[::-1]
        return print(n, '--->', reverso)
    else:
        erro = '\033[031mErro! Por favor, digite um número inteiro.\033[m'
        return print(erro)


print('~' * 40)
print('REVERSO DE UM NÚMERO'.center(40))
print('~' * 40)
while True:
    num = str(input('Digite um número inteiro: '))
    print('~' * 40)
    if num.isnumeric():
        break
    leiaint(num)
print('Imprimindo o número invertido...')
sleep(2)
leiaint(num)
