n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
for c in range(n1 + 1, n2):
    print(c, end=' - ' if c < n2 - 1 else'')