"""[NOME DO SEU JOGO]"""

""" importa as bibliotecas necessárias"""
import sys, pygame

#Inicia o pygame
pygame.init()

#define a tela do jogo
size = width, height = 320, 240
speed = [2,2]
black = 0,0,0
screen= pygame.display.set_mode(size)
#ESTRUTURA ADICIONADA NO ARQUIVO COMPLETO DO JOGO

#carrega imagem dos elementos do jogo
#SEM IMAGENS

#[CARREGUE AQUI AS IMAGENS DOS SEUS ELEMENTOS ]
#exemplo:
ball = pygame.image.load("balao.jpg")
ballrect = ball.get_rect()

#Laço infinito onde acontece todos os eventos do jogo
while True:

    #laço de eventos do jogo
    for event in pygame.event.get():
        #tratamento do evento sair do jogo
        if event.type == pygame.QUIT:
            sys.exit()
    #LAÇOS FEITOS NO ARQUIVO DO JOGO
    
    #lógica(eurística) do seu jogo
    #[O PRIMEIRO JOGADOR A COMPLETAR A SEQUÊNCIA PRIMEIRO VENCE]


    #preenche a tela com preto
    screen.fill(black)
    #atualiza a posição do retângulo do elemento no buffer que será mostrado no frame seguinte
    #[FAÇA A ATUALIZAÇÂO DA POSIÇÂO DOS ELEMENTOS DO SEU JOGO AQUI]
    #exemplo:
    #screen.blit(ball,ballrect)
    #screen.blit(guitar,guitarrect)
    #...

    #atualiza a tela 
    pygame.display.flip()