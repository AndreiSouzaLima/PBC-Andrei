usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    identidade = input("Digite a identidade do usuário: ")
    codigo = len(usuarios) + 1
    usuario = {"codigo": codigo, "nome": nome, "idade": idade, "identidade": identidade}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso! Código: ", codigo)

def pesquisar_usuario():
    codigo = int(input("Digite o código do usuário que deseja pesquisar: "))
    for usuario in usuarios:
        if usuario["codigo"] == codigo:
            print(usuario)
            break
    else:
        print("Usuário não encontrado.")

def remover_usuario():
    codigo = int(input("Digite o código do usuário que deseja remover: "))
    for i, usuario in enumerate(usuarios):
        if usuario["codigo"] == codigo:
            del usuarios[i]
            print("Usuário removido com sucesso!")
            break
    else:
        print("Usuário não encontrado.")

while True:
    print("\nMenu:")
    print("1. Cadastrar usuário")
    print("2. Pesquisar usuário por código")
    print("3. Remover usuário por código")
    print("0. Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        pesquisar_usuario()
    elif opcao == "3":
        remover_usuario()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")