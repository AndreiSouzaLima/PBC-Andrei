#Escreva um programa Python que leia uma lista de números e calcule a média dos números.
numeros = input("Digite uma lista de números separados por espaço: ")
numeros = [float(x) for x in numeros.split()]

media = sum(numeros) / len(numeros)

print(f"A média dos números é: {media:.2f}")