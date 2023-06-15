def contar(frase, caracter):
    cont = 0
    for c in range(0, len(frase)):
        if frase[c] == caracter:
            cont += 1
    return cont


frase = str(input('Digite uma frase: ')).lower()
espaços = contar(frase, ' ')
a = contar(frase, 'a')
e = contar(frase, 'e')
i = contar(frase, 'i')
o = contar(frase, 'o')
u = contar(frase, 'u')
print('Número de espaços:', espaços)
print('Número de a:', a)
print('Núemro de e:', e)
print('Número de i:', i)
print('Número de o:', o)
print('Número de u:', u)
