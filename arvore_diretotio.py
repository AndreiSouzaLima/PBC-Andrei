#Escreva um programa Python que gere uma árvore de diretórios a partir de uma lista de diretórios e arquivos.
import os

def gerar_arvore(diretorio, nivel=0):
    lista = os.listdir(diretorio)

    for arquivo in lista:
        if os.path.isdir(os.path.join(diretorio, arquivo)):
            print("|  " * nivel + "+--" + arquivo)
            gerar_arvore(os.path.join(diretorio, arquivo), nivel+1)
        else:
            print("|  " * nivel + "+--" + arquivo)

lista = [
    "diretorio1/",
    "diretorio2/",
    "arquivo1.txt",
    "diretorio1/arquivo2.txt",
    "diretorio2/diretorio3/",
    "diretorio2/diretorio3/arquivo3.txt",
]

for item in lista:
    if item.endswith("/"):
        os.makedirs(item, exist_ok=True)
    else:
        with open(item, 'w') as f:
            f.write("Conteúdo do arquivo {}.\n".format(item))

print(".")
gerar_arvore(".", 0)