def valorPagamento(valor, dias):
        if dias == 0:
            tot = valor
        elif dias > 0:
            tot = valor + (valor * 3 / 100) + 0.1 / 100 * dias
        print('~' * 50)
        print(f'O valor da prestação a ser pago é de R${tot:.2f}')


soma = cont = 0
print('=' * 50)
print(f'{"CALCULANDO PRESTAÇÕES":^50}')
while True:
    print('=' * 50)
    v = float(input('Valor da prestação: (0 para encerrar) '))
    soma += v
    if v == 0:
        break
    else:
        d = int(input('Número de dias de atraso: '))
        valorPagamento(v, d)
        cont += 1
print('=' * 65)
print(f'Ao todo foram pagas {cont} prestações com um valor total de R${soma:.2f}.')
print('=' *65)
print('<<< Obrigado, volte sempre! >>>')
