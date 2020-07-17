import pygame

pygame.init()
x = 400
y = 300
pos_x = 200
pos_y = 300
velocidade = 10
fundo = pygame.image.load('rua.png')
carro = pygame.image.load('carroyellow.png')
azul = pygame.image.load('carroazull.png')
red = pygame.image.load('carroredd.png')
roxo = pygame.image.load('carroroxoo.png')
velocidade_outros = 20

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("meu primeiro jogo")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    if (pos_y <= -200):
        pos_y = 600
    pos_y -= velocidade_outros

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(azul,(pos_x, pos_y))
    janela.blit(red,(pos_x + 140, pos_y))
    janela.blit(roxo,(pos_x +270, pos_y))
    pygame.display.update()
pygame.quit()