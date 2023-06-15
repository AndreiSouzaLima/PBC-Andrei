def somaImposto(taxaImposto, custo):
    total = custo + (custo * taxaImposto / 100)
    return total


t = float(input('Digite a taxa de imposto: '))
c = float(input('Digite o custo: '))
resultado = somaImposto(t, c)
print(f'A soma do imposto é:', resultado)