def data(d):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
             'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
    if d[0].isnumeric():
        n = d.split('/')
        a = int(n[1])
        print(f'Você nasceu em {n[0]} de {meses[a-1]} de {n[2]}')


while True:
    dt = str(input('Digite sua data de nascimento: (DD/MM/AAAA) '))
    data(dt)
    if dt[0].isnumeric():
        break
    else:
        print('ERRO! Data inválida')
