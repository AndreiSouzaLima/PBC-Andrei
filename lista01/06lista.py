n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor digitado foi o {maior}')
