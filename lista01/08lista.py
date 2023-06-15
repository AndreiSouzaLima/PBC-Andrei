p1 = float(input('Preço do primeiro produto: R$'))
p2 = float(input('Preço do segundo produto: R$'))
p3 = float(input('Preço do terceiro produto: R$'))
menor = p1
if p2 < p1 and p2 < p3:
    menor = p2
if p3 < p1 and p3 < p2:
    menor = p3
print(f'O produto que custa R${menor:.2f} é o mais aconselhado a se comprar, devido ao seu preço.')