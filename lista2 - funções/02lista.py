def digitos(d):
    lista = []
    a = str(d)
    if a.isnumeric():
        lista.append(a)
        quant = len(a)
        return print(f'O número {d} tem {quant} dígitos.')


while True:
    print('=' * 40)
    n = str(input('Digite um número: '))
    digitos(n)
    if n.isnumeric():
        break
    else:
        print('ERRO! Digite apenas números inteiros')
print('=' * 40)
print(' <<< FIM >>>')
