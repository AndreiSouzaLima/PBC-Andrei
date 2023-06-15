print('='*30)
print(f'{"Sequência de Fibonacci":^30}')
print('='*30)
n = 0
n1 = 0
n2 = 1
print(f' {n1} - {n2} ', end=' - ')
while True:
    n3 = n1 + n2
    print(n3, end=' - ' if n3 < 500 else '')
    n1 = n2
    n2 = n3
    n += 1
    if n3 > 500:
        break