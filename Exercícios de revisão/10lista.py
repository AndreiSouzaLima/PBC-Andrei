def sortear(jogador=0, jogada=0):
    from time import sleep
    from random import randint
    jogador = randint(2, 12)
    jogada = 1
    print('=' * 40)
    print(f'{"--> 1º rodada":^10}')
    while True:
        if jogador == 7 or jogador == 11:
            print(f'Você tirou o número {jogador} e ganhou!')
            break
        elif jogador == 2 or jogador == 3 or jogador == 12:
            print(f'Você tirou o número {jogador} e perdeu!')
            break
        else:
            ponto = jogador
            print(f'Você tirou o número {jogador}')
            sleep(1.5)
            while True:
                jogada += 1
                sleep(1.5)
                print('=' * 40)
                print(f'{f"--> {jogada}º rodada":^10}')
                jogador = randint(2, 12)
                if jogador == ponto:
                    print(f'Você tirou o número {jogador} e foi igual a primeira rodada. Você ganhou!')
                    break
                elif jogador == 7:
                    print(f'Você tirou o número 7 antes de repetir seu ponto. Você perdeu! ')
                    break
                else:
                    print(f'Você tirou o número {jogador}')
        break
    sleep(1.5)
    print('~' * 40)
    print('Finalizando...')
    print('~' * 40)
    sleep(2)
    print('<<<< FIM DO PROGRAMA >>>>')


sortear()
