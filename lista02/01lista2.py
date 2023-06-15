cont = 0
while True:
    nota = float(input('Digite uma nota entre 0 e 10: '))
    cont += 1
    if nota >= 0 and nota <= 10:
        break
print('Obrigado pela informação!')