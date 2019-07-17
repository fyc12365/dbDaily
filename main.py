import os
import pygame
import time
from pygame.locals import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('有点儿正常的大冒险')
icon = pygame.image.load('Data/image/icon.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('Data/image/bg.png')
button_start = pygame.image.load('Data/image/start.png')
scene_1_bg = pygame.image.load('Data/image/scene_1_bg.png')
block_ = pygame.image.load('Data/image/block.png')
mouse_replace = pygame.image.load('Data/image/mouse.png')
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

def main_menu():
    pygame.mixer.music.load('Data/music/menu_bgm.mp3')
    pygame.mixer.music.play(1,0)
    buloon_1 = 0
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN and 275<=event.pos[0]<=525 and 400<=event.pos[1]<=500 :
                buloon_1 = 1
                pygame.mixer.music.stop()
                break
        if buloon_1 == 1:
            break
        screen.blit(bg,(0,0))
        screen.blit(button_start,(275,400))
        x, y = pygame.mouse.get_pos()
        screen.blit(mouse_replace,(x,y))
        pygame.display.update()

def scene_1():
    pygame.mixer.music.load('Data/music/scene_1_bgm.mp3')
    pygame.mixer.music.play(1,0)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if 16<=event.pos[0]<=43 and 295<=event.pos[1]<=322:
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                exit()
                        screen.blit(scene_1_bg,(0,0))
                        screen.blit(block_,(0,0))
                        x,y = pygame.mouse.get_pos()
                        screen.blit(mouse_replace,(x,y))
                        pygame.display.update()
        screen.blit(scene_1_bg,(0,0))
        x,y = pygame.mouse.get_pos()
        screen.blit(mouse_replace,(x,y))
        pygame.display.update()

main_menu()
scene_1()

os.system('pause')