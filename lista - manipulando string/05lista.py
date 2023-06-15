from time import sleep
print('~' * 50)
print('Imprimindo nome em forma de escada invertida'.center(50))
print('~' * 50)
nome = str(input('Digite seu nome: ')).upper()
print('~' * 50)
print('Imprimindo seu nome...')
sleep(1)
c = 0
for c in range(len(nome), 0, -1):
    print(nome[:c])
    sleep(1)
print('<<< Pronto! >>>')
