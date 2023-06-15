
class Node:
    def __init__(self ,value, nivel=0):
        self.value =value
        self.right =None
        self.left =None
        self.nivel = nivel

class Tree:
    def __init__(self):
        self.root =None
        self.altura = 0

    def insert(self ,value):
        self._insert(value ,self.root)

    def _insert(self ,value ,atual=None):

        if self.root == None:
            self.root =Node(value, 1)
            atual = self.root
            atual.value =value
        else:
            if atual!= None:
                if value >= atual.value:
                    if atual.right==None:
                        atual.right = Node(value, atual.nivel+1)
                    else:
                        self._insert(value, atual.right)
                else:
                    if atual.left==None:
                        atual.left = Node(value, atual.nivel+1)
                    else:
                        self._insert(value, atual.left)

    def print(self):
        self._print(self.root)

    def _print(self, atual=None):

        if atual != None:
            print(str(atual.value) + ':' + str(atual.nivel) + ",")

            self._print(atual.left)
            self._print(atual.right)

    def calcAltura(self):
        return self._calcAltura(self.root)

    def _calcAltura(self, atual, nivel):
        if self.root == None:
            self.altura = 0
        else:
            if atual != None:

                if nivel < atual.nivel:
                    self.altura = atual.nivel

                self._calcAltura(atual.left)
                self._calcAltura(atual.right)
        return self.altura

if __name__ == '__main__':
    tree =Tree()
    command = ""
    while command != "s":

        command =input("inserir(i),print(p):")

        if command == "i":
            value = float(input("digite um número:"))
            tree.insert(value)
        else:
            if command == "p":
                tree.print()

print("saiu")
