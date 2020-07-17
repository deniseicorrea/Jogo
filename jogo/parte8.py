import pygame
from random import randint
pygame.init()
x = 350  #max 530 min 230
y = 180
pos_x = 200
pos_y = 800
pos_ya = 800
pos_yc = 800   #carro do meio
timer = 0
tempo_segundo = 0

velocidade_outros = 12
velocidade = 10
fundo = pygame.image.load('rua.png')
carro = pygame.image.load('carroyellow.png')
azul = pygame.image.load('carroazull.png')
vermelho = pygame.image.load('carroredd.png')
roxo = pygame.image.load('carroroxoo.png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Meu primeiro jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x <= 530:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 140:
        x -= velocidade

    #detecta a colisao
    if ((x + 80 > pos_x and y+ 180 > pos_y)):  #lado direito
       y = 1200

    if ((x - 80 < pos_x - 300 and y + 180 > pos_ya)): #colisao lado esquerdo
        y = 1200
# colisao central
    if (x + 80 > pos_x and y + 180 > pos_y) or  (x - 80 < pos_x - 300 and y + 180 > pos_ya):
        y= 1200
    if (pos_y <= -80) :
       pos_y = randint(800,1000)

    if ((pos_ya <= -80)):
       pos_ya = randint(1300,2000)

    if ((pos_yc <= -80)) :
       pos_yc = randint(2200,3000)

    if (timer < 20):
        timer += 1
    else:
        tempo_segundo +=1
        texto = font.render("Tempo: "+ str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y -= velocidade_outros
    pos_ya -= velocidade_outros +2
    pos_yc -= velocidade_outros + 10

    janela.blit(fundo, (0,0))
    janela.blit(carro,(x,y))
    janela.blit(azul,(pos_x, pos_y))
    janela.blit(vermelho,(pos_x -300, pos_ya))
    janela.blit(roxo, (pos_x -136, pos_yc))
    janela.blit(texto,pos_texto)
    pygame.display.update()


pygame.quit()