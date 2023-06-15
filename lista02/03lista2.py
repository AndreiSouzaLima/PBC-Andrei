print('-'*50)
print(f'{"VALIDANDO DADOS":^50}')
print('-'*50)
while True:
    nome = str(input('Nome: '))
    palavra = len(nome)
    while palavra < 3:
        print('Erro! Nome deve ter mais que 3 caracteres. Tente novamente.')
        print('-' * 50)
        nome = str(input('Nome: '))
        palavra = len(nome)
    print('-' * 50)
    idade = int(input('Idade: '))
    while idade < 0 or idade > 150:
        print('Erro! A idade deve ser entre 0 e 150. Tente novamente. ')
        print('-' * 50)
        idade = int(input('Idade: '))
    print('-' * 50)
    salário = float(input('Salário: R$ '))
    while salário < 0:
        print('Erro! O salário deve ser maior que zero. Tente novamente. ')
        print('-' * 50)
        salário = float(input('Salário: R$ '))
    print('-' * 50)
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo not in 'MF':
        print('Erro! Tente novamente.')
        print('-' * 50)
        sexo = str(input('Sexo: [M/F] ')).upper()
    print('-' * 50)
    estciv = str(input('Estado cívil: [S/C/V/D] ')).upper()
    while estciv not in 'SCVD':
        print('Erro! Tente novamente.')
        print('-' * 50)
        estciv = str(input('Estado cívil: [S/C/V/D] ')).upper()
    print('-' * 50)
    break
print('Todas as informações foram validadas. Obrigado por informá-las!')
