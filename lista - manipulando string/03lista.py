from time import sleep
print('~' * 35)
print('Imprimindo nome'.center(35))
print('~' * 35)
nome = str(input('Digite seu nome: ')).upper()
print('~' * 35)
print('Imprimindo seu nome...')
sleep(1)
for c in range(0, len(nome)):
    print(nome[c])
    sleep(1)
print('<<< Pronto! >>>')