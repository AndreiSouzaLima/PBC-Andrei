#Escreva um programa Python que leia um arquivo de texto e substitua todas as ocorrências de uma palavra por outra palavra.
arquivo = input("Digite o nome do arquivo: ")
palavra_antiga = input("Digite a palavra antiga: ")
palavra_nova = input("Digite a palavra nova: ")

with open(arquivo, 'r') as f:
    conteudo = f.read()

conteudo_modificado = conteudo.replace(palavra_antiga, palavra_nova)

with open(arquivo, 'w') as f:
    f.write(conteudo_modificado)

print("Substituição concluída.")