print('='*50)
print(f'{"NÚMERO DE HABITANTES":^50}')
print('='*50)
print('Insira os dados abaixo para saber em quantos anos', end='')
print('\no país A ultrapassará o país B')
print('-'*50)
popa = float(input('Informe a população de um país A: '))
popb = float(input('Informe a população de um país B: '))
cresa = float(input('Informe a taxa de crescimento do país A (ao ano): '))
cresb = float(input('Informe a taxa de crescimento do país B (ao ano): '))
print('-'*50)
anos = 0
resp = ' '
if popa < popb:
    while True:
        popa = popa + (popa * cresa / 100)
        popb = popb + (popb * cresb / 100)
        anos += 1
        if popa > popb:
            print(f'Após {anos} anos o país A ultrapassará o país B em número de habitantes.')
            print(f'A população do país A será de {popa:.0f} e a do país B será de {popb:.0f}.')
            print('-'*50)
            resp = str(input('Deseja fazer novamente? [S/N] ')).upper()
            print('-'*50)
            if resp == 'S':
                popa = float(input('Informe a população de um país A: '))
                popb = float(input('Informe a população de um país B: '))
                cresa = float(input('Informe a taxa de crescimento do país A (ao ano): '))
                cresb = float(input('Informe a taxa de crescimento do país B (ao ano): '))
                if popa > popb:
                    print('-'*50)
                    print('O número de habitantes do país A já é superior ao do país B. ')
                    print('-'*50)
                    break
            if resp == 'N':
                break
else:
    print('O número de habitantes do país A já é superior ao do país B. ')
    print('-'*50)
print('Fim do programa. Volte sempre! ')