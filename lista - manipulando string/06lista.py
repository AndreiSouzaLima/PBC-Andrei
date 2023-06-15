lista = []
nasc = str(input('Data de nascimento(dd/mm/aaaa): '))
data = nasc.split('/')
lista2 = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
          'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
          'Novembro', 'Dezembro']
meses = int(data[1])
mês = lista2[meses - 1]
print(f'Você nasceu em {data[0]} de {mês} de {data[2]}.')
