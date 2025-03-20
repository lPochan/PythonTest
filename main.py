from operator import truediv

import pygame
import arcade
import os
import random


pygame.init()
x = 450
y = 300

velocidade = 10


#Tamanho da Janela principal do jogo
janela = pygame.display.set_mode((900,600))
#Título do jogo
pygame.display.set_caption("Jogo")

#Atualização e Configuração para manter a janela aberta
janela_aberta = True
while janela_aberta :

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

    janela.fill((0,0,0))
    #Caracteristicas do Objeto principal (Cor RGB , Localização , Tamanho)
    pygame.draw.circle(janela, (255,0,0) , (x , y), 50)
    pygame.display.update()
pygame.quit()


