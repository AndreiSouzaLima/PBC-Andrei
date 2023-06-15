class  ContaBancaria:
    def __init__(self, cpf):
        self.registro = []
        self.saldo = 0.0
        self.registro.append(self.saldo)
        self.cpf = cpf

    def depositar(self, valor):
        self.saldo += valor
        self.registro.append(valor)

    def sacar(self, valor):
        self.saldo +=- valor
        self.registro.append(valor)

    def extrato(self):
        print(f'Saldo anterior                 R${self.registro[0]:.2f}')
        print(f'Deposito                       R${self.registro[1]:.2f}')
        print(f'Saque                          R${self.registro[2]:.2f}')
        print(f'Saldo atual:                   R${self.saldo:.2f}')

    def linha(self):
        print('=' * 40)

    def titulo(self):
        self.linha()
        print('EXTRATO BANCÁRIO'.center(40))
        self.linha()


contaBancaria = ContaBancaria("04067232876")
contaBancaria.titulo()
contaBancaria.depositar(10)
contaBancaria.sacar(2.5)
contaBancaria.extrato()
contaBancaria.linha()
