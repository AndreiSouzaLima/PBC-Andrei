maior = 0
for c in range(0, 5):
    n = float(input('Digite um número: '))
    c += 1
    if n > maior:
        maior = n
print('Você digitou 5 números e o maior deles foi o', maior)
