def argumento(valor):
    if valor > 0:
        valor = 'P'
    else:
        valor = 'N'
    return valor


n = int(input('Digite um número: '))
print(argumento(n))