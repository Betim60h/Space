import pygame
import sys
from tkinter import simpledialog


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('space.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

pygame.init()
tamanho = (1280, 720)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
fundo = pygame.image.load("space.jpg").convert()  
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Space")
fundo = pygame.transform.scale(fundo, tamanho)
play_music ()

branco = (255,255,255)
font = pygame.font.Font (None, 36)



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "nome do planeta")
            print(item)
            if item is None:
                item = "desconhecido" + str(pos)
                estrelas[item] = pos
    tela.fill((branco))
    tela.blit(fundo, (0, 0))  
    F10 = font.render ("Pressione F10 para salvar os pontos", True, branco)
    F11 = font.render ("Pressione F11 para carregar os pontos", True, branco)
    F12 = font.render ("Pressione F12 para deletar os pontos", True, branco)
    tela.blit(F10, (10,10))
    tela.blit(F11, (10,35)) #widht #height
    tela.blit(F12, (10,60))



    pygame.display.update()
    clock.tick(60)
