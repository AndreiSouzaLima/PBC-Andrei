carros = []
funcionarios = []
clientes = []

def cadastrar_carro():
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = input("Digite o ano do carro: ")
    cor = input("Digite a cor do carro: ")
    preco = input("Digite o preço do carro: ")
    codigo = input("Digite o código do carro: ")
    carro = {'marca': marca, 'modelo': modelo, 'ano': ano, 'cor': cor, 'preco': preco, 'codigo': codigo}
    carros.append(carro)
    print("Carro cadastrado com sucesso!")

def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    sobrenome = input("Digite o sobrenome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    telefone = input("Digite o telefone do funcionário: ")
    endereco = input("Digite o endereço do funcionário: ")
    codigo = input("Digite o código do funcionário: ")
    funcionario = {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'telefone': telefone, 'endereco': endereco, 'codigo': codigo}
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    sobrenome = input("Digite o sobrenome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    codigo = input("Digite o código do cliente: ")
    cliente = {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'telefone': telefone, 'endereco': endereco, 'codigo': codigo}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def pesquisar_carro():
    codigo = input("Digite o código do carro: ")
    for carro in carros:
        if carro['codigo'] == codigo:
            print("Marca:", carro['marca'])
            print("Modelo:", carro['modelo'])
            print("Ano:", carro['ano'])
            print("Cor:", carro['cor'])
            print("Preço:", carro['preco'])
            return
    print("Carro não encontrado.")

def pesquisar_funcionario():
    codigo = input("Digite o código do funcionário: ")
    for funcionario in funcionarios:
        if funcionario['codigo'] == codigo:
            print("Nome:", funcionario['nome'])
            print("Sobrenome:", funcionario['sobrenome'])
            print("CPF:", funcionario['cpf'])
            print("Telefone:", funcionario['telefone'])
            print("Endereço:", funcionario['endereco'])
            return
    print("Funcionário não encontrado.")

def pesquisar_cliente():
    codigo = input("Digite o código do cliente: ")
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            print("Nome:", cliente['nome'])
            print("Sobrenome:", cliente['sobrenome'])
            print("CPF:", cliente['cpf'])
            print("Telefone:", cliente['telefone'])
            print("Endereço:", cliente['endereco'])
            return
    print("Cliente não encontrado.")
def remover_carro():
    codigo = input("Digite o código do carro a ser removido: ")
    for carro in carros:
        if carro['codigo'] == codigo:
            carros.remove(carro)
            print("Carro removido com sucesso!")
            return
            print("Carro não encontrado.")

def remover_funcionario():
    codigo = input("Digite o código do funcionário a ser removido: ")
    for funcionario in funcionarios:
        if funcionario['codigo'] == codigo:
            funcionarios.remove(funcionario)
            print("Funcionário removido com sucesso!")
            return
            print("Funcionário não encontrado.")

def remover_cliente():
    codigo = input("Digite o código do cliente a ser removido: ")
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            clientes.remove(cliente)
            print("Cliente removido com sucesso!")
            return
            print("Cliente não encontrado.")

while True:
    print("Menu de Cadastro de Concessionária:")
    print("1. Cadastro de Carros")
    print("2. Cadastro de Funcionários")
    print("3. Cadastro de Clientes")
    print("4. Pesquisar Carros")
    print("5. Pesquisar Funcionários")
    print("6. Pesquisar Clientes")
    print("7. Remover Carros")
    print("8. Remover Funcionários")
    print("9. Remover Clientes")
    print("10. Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == '1':
        cadastrar_carro()
    elif opcao == '2':
        cadastrar_funcionario()
    elif opcao == '3':
        cadastrar_cliente()
    elif opcao == '4':
        pesquisar_carro()
    elif opcao == '5':
        pesquisar_funcionario()
    elif opcao == '6':
        pesquisar_cliente()
    elif opcao == '7':
        remover_carro()
    elif opcao == '8':
        remover_funcionario()
    elif opcao == '9':
        remover_cliente()
    elif opcao == '10':
        print("Saindo...")
    break
else:
    print("Opção inválida. Digite novamente.")