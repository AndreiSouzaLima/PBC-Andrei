def linha(tam=50, s='='):
    return s * tam


print(linha(50, '~'))
print('Comparar duas frases'.center(50))
print(linha(50, '~'))
s1 = str(input('Primeira frase: '))
s2 = str(input('Segunda frase: '))
print(linha())
print(f'Tamanho de "{s1}": {len(s1)} caracteres')
print(f'Tamanho de "{s2}": {len(s2)} caracteres')
t1 = len(s1)
t2 = len(s2)
print(linha())
if t1 == t2:
    print('As duas frases são de tamanhos iguais.')
else:
    print('As duas frases são de tamanhos diferentes.')
print(linha(50, '-'))
if s1.lower() == s2.lower():
    print('As duas frases possuem o mesmo conteúdo.')
else:
    print('As duas frases possuem conteúdos diferentes.')
print(linha())
print(' <<< FIM >>>')
