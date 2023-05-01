#Escreva um programa Python que leia um arquivo de texto e conte a frequência de cada palavra no arquivo.
arquivo = input("Digite o nome do arquivo: ")

try:
    with open(arquivo, 'r') as f:
        palavras = f.read().split()
        frequencia = {}
        for palavra in palavras:
            if palavra in frequencia:
                frequencia[palavra] += 1
            else:
                frequencia[palavra] = 1
        
        print("Frequência de palavras no arquivo:")
        for palavra, freq in frequencia.items():
            print(f"{palavra}: {freq}")
except FileNotFoundError:
    print("Arquivo não encontrado.")