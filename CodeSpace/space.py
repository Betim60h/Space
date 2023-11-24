
#Roberto Jacobs 
#Ra: 1135584

#Henique Daros
#1135569




import pygame
import sys
import json
from tkinter import simpledialog
import tkinter as tk
import math
import time

def calcular_distancia(p1, p2):
    return math.dist(p1, p2)

def inicializar():
    try:
        with open('Space.txt', 'r') as arquivo:
            global estrelas
            estrelas = json.load(arquivo)
    except FileNotFoundError:
        estrelas = {}

def salvar():
    with open('Space.txt', 'w') as arquivo:
        json.dump(estrelas, arquivo)

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('space.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def carregar():
    try:
        with open('Space.txt', 'r') as arquivo:
            global estrelas
            estrelas = json.load(arquivo)
    except FileNotFoundError:
        estrelas = {}
caminho_icone = "logo.ico"
pygame.init()
tamanho = (1280, 720)
clock = pygame.time.Clock()
tela = pygame.display.set_mode((tamanho))
fundo = pygame.image.load("space.jpg").convert()
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("SpaceMaker")
fundo = pygame.transform.scale(fundo, tamanho)
play_music()
verde = (59, 242, 95)
branco = (255, 255, 255)
font = pygame.font.Font(None, 36)
estrelas = {}
f12 = False
f10 = False
Esc = 0
Fechar = 1
salvando = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Esc = True
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Digite o nome do planeta")

            if item is not None:  
                nome_planeta = item.strip() if item.strip() != "" else "Planeta desconhecido" + str (pos)
                estrelas[nome_planeta] = pos
                mensagem = f"{nome_planeta}: {pos}"
                mensagem_renderizada = font.render(mensagem, True, branco)

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_F12:
                f12 = True
            elif evento.key == pygame.K_F10:
                f10 = True
                salvando = False
                salvar ()
            elif evento.key == pygame.K_F11:
                carregar()
            if evento.key == pygame.K_ESCAPE:
                 Esc += 1
                 if Esc >= Fechar :
                  salvar ()
                  time.sleep (1)
                  pygame.quit()
                  sys.exit()

    tela.fill((branco))
    tela.blit(fundo, (0, 0))
    F10 = font.render("Pressione F10 para salvar os pontos", True, branco)
    F11 = font.render("Pressione F11 para carregar os pontos", True, branco)
    F12 = font.render("Pressione F12 para deletar os pontos", True, branco)
    font2 = pygame.font.Font(None, 24)
    ESC = font2.render("pressione ESC 2 vezes para fechar", True, branco)
    tela.blit(F10, (10, 10))
    tela.blit(F11, (10, 35))  # ((largura)x (altura) )
    tela.blit(F12, (10, 60))
    tela.blit (ESC,(1000,10))
    for nome, posicao in estrelas.items():
        pygame.draw.circle(tela, branco, posicao, 10)
        texto_estrela = font.render(nome, True, branco)
        tela.blit(texto_estrela, (posicao[0] + 20, posicao[1] - 10))

    if len(estrelas) > 1:
        pontos = list(estrelas.values())
        pygame.draw.lines(tela, branco, False, pontos, 2)

        for i in range(len(pontos) - 1):
            p1 = pontos[i]
            p2 = pontos[i + 1]
            meio_x = (p1[0] + p2[0]) // 2
            meio_y = (p1[1] + p2[1]) // 2
            distancia = calcular_distancia(p1, p2)
            texto_distancia = font.render(f"{distancia:.2f} Distancia (KM)", True, verde)
            tela.blit(texto_distancia, (meio_x, meio_y))
    
    
    
    if salvando == False:
        salvar()
        font3 = pygame.font.Font(None, 40)
        SAVE = font3.render("Salvando...", True, branco)
        tela.blit(SAVE, (540, 10)) # ((largura)x (altura) )
        time.sleep (1)
        salvando = True
    if f12 and estrelas:
        ultima_estrela = list(estrelas.keys())[-1]
        del estrelas[ultima_estrela]
        f12 = False


    pygame.display.update()
    clock.tick(60)
