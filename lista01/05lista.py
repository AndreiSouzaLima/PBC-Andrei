n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
m = (n1 + n2) / 2
if m >= 7 and m != 10:
    print('Você foi Aprovado. Parabéns! ')
if m < 7:
    print('Você foi reprovado. Estude mais! ')
if m == 10:
    print('Você foi aprovado com distinção. Excelente! ')