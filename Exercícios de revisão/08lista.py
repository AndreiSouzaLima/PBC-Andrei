def leiaint(n):
    if n.isnumeric():
        tam = len(n)
        return print('No número',n,'há', tam,'dígitos.')
    else:
        erro = '\033[031mErro! Por favor, digite um número inteiro.\033[m'
        return print(erro)


while True:
    num = str(input('Digite um número inteiro: '))
    if num.isnumeric():
        break
    leiaint(num)
leiaint(num)
