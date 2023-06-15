class pilha:
    def __init__(self):
        self.p = []

    def inserir(self, i):
        self.p.append(i)

    def ver(self):
        return print(f'No topo da pilha está o elemento "{self.p[len(self.p)-1]}"')

    def deletar(self):
        return print(f'O elemento "{self.p.pop()}" foi deletado ')


ins = pilha()
while True:
    x = str(input('Digite algo para a pilha: '))
    resp = str(input('Quer continuar?: [S/N] ')).upper()
    ins.inserir(x)
    if resp == 'N':
        ins.ver()
        pergunta = str(input('Deseja deletar: [S/N] ')).upper()
        if pergunta == 'S':
            ins.deletar()
        break
print('<<< FIM >>>')
