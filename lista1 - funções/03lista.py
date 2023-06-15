def argumentos(a1=0, a2=0, a3=0):
    s = a1 + a2 + a3
    print(f'A soma dos números é {s}')
    return s


print('=' * 30)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('=' * 30)
argumentos(n1, n2, n3)
