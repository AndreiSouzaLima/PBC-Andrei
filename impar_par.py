#Escreva um programa Python que receba como entrada um número inteiro e retorne True 
#se ele for par ou False se for ímpar.
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
    resultado = True
else:
    print("O número é ímpar.")
    resultado = False

print(f"Resultado: {resultado}")