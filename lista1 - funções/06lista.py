def conversão(horas, minutos):
    horas2 = 0
    if horas >= 12:
        if horas > 12:
            horas2 = horas - 12
            ampm = 'P.M'
        elif horas == 12:
            horas2 = horas
            ampm = 'P.M'
    elif horas < 12 and 0 < minutos < 60:
        horas2 = horas
        ampm = 'A.M'
    elif horas == 00:
        horas2 = 12
        ampm = 'A.M'
    if 0 <= minutos <= 9:
        return print(f'A conversão para A.M/P.M é: {horas2}:0{minutos} {ampm}')
    else:
        return print(f'A conversão para A.M/P.M é: {horas2}:{minutos} {ampm}')


print('=' * 40)
print(f'{"CONVERSOR DE HORAS":^40}')
while True:
    print('=' * 40)
    h = int(input('Digite as horas: '))
    m = int(input('Digite os minutos: '))
    while True:
        if 0 <= h <= 24:
            break
        else:
            while True:
                print('ERRO! Tente novamente')
                h = int(input('Digite as horas: '))
                if 0 <= h <= 24:
                    break
        if 0 <= m <= 60:
            break
        else:
            while True:
                print('ERRO! Tente novamente')
                m = int(input('Digite os minutos: '))
                if 0 <= m <= 60:
                    break
    print('-' * 40)
    conversão(h, m)
    print('-' * 40)
    resp = str(input('Deseja continuar: [S/N] '))
    while True:
        if resp in 'SsNn':
            break
        else:
            print('ERRO! Tente novamente')
            resp = str(input('Deseja continuar: [S/N] '))
    if resp in 'Nn':
        break
print('=' * 40)
print('<<< FIM DO PROGRAMA! >>>')
