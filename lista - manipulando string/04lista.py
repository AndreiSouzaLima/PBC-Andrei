from time import sleep
print('~' * 45)
print('Imprimindo nome em forma de escada'.center(45))
print('~' * 45)
nome = str(input('Digite seu nome: ')).upper()
print('~' * 45)
print('Imprimindo seu nome...')
sleep(1)
c = 1
for c in range(1, len(nome)+1):
    print(nome[:c])
    sleep(1)
print('<<< Pronto! >>>')
