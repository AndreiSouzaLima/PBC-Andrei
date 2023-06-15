n = soma = média = 0
for c in range(1, 6):
    n = int(input(f'{c}ª número: '))
    c += 1
    soma += n
média = soma/5 
print('A soma dos números digitados é', soma, 'e a média entre eles é de', média)
