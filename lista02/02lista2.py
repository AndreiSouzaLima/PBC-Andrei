senha = nome = ' '
while nome == senha:
    nome = str(input('Digite seu nome: '))
    senha = str(input('Digite sua senha: '))
    if senha == nome:
        print('Impossível cadastrar-se com nome e senha iguais. Tente novamente!')
print('Cadastrado! Obrigado pelas informações.')
