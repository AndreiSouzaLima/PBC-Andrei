from time import sleep
print('~' * 40)
print('DETECTOR DE PALÍNDROMO'.center(40))
print('~' * 40)
frase = str(input('Digite uma frase: ')).lower()
separar = frase.split()
juntar = ''.join(separar)
inverter = juntar[::-1]
print(f'A frase digitada foi "{frase}".')
sleep(1.5)
print('~' * 40)
print('Invertendo...')
print('~' * 40)
sleep(2)
print(f'A frase invertida fica "{inverter}"')
sleep(1.5)
if juntar == inverter:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo.')
print('~' * 40)
sleep(1.5)

