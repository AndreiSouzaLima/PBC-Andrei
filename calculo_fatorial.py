#Escreva um programa Python que leia um número inteiro e calcule o fatorial desse número.
numero = int(input("Digite um número inteiro: "))
fatorial = 1

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, numero+1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}.")