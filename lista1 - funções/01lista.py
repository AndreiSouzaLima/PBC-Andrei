def linha(n):
    for c in range(n + 1):
        for i in range(c):
            print(c, end=' ')
        print()


n = int(input('Digite um número: '))
linha(n)



