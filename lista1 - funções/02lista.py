def linha2(n):
    s = ''
    for i in range(1, n+1):
        s += str(i) + ' '
    s += '\n'
    return s


def linha1(n):
    s = ''
    for i in range(1, n+1):
        s += linha2(i)
    return s


n = int(input('Digite um número: '))
resultado = linha1(n)
print(resultado)


