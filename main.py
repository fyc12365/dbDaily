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
error_1 = pygame.image.load('Data/image/error_1.jpg')
mouse_replace = pygame.image.load('Data/image/mouse.png')
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

def main_menu():
    pygame.mixer.music.load('Data/music/menu_bgm.ogg')
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
        
textFont_1 = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',50)
text_1 = textFont_1.render('好好学一学数学！智商-10',True,(0,0,0))

def scene_1():
    buloon_1 = 0
    pygame.mixer.music.load('Data/music/scene_1_bgm.ogg')
    pygame.mixer.music.play(1,0)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                try:
                    if 16<=event.pos[0]<=43 and 295<=event.pos[1]<=322:
                        timer_0 = time.time()
                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    exit()
                            if time.time() >= timer_0+5:
                                break
                            screen.blit(scene_1_bg,(0,0))
                            screen.blit(block_,(0,0))
                            screen.blit(error_1,(260,210))
                            screen.blit(text_1,(120,180))
                            x,y = pygame.mouse.get_pos()
                            screen.blit(mouse_replace,(x,y))
                            pygame.display.update()
                    if 16<=event.pos[0]<=43 and 383<=event.pos[1]<=410:
                        timer_0 = time.time()
                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    exit()
                            if time.time() >= timer_0+5:
                                break
                            screen.blit(scene_1_bg,(0,0))
                            screen.blit(block_,(0,0))
                            screen.blit(error_1,(260,210))
                            screen.blit(text_1,(120,180))
                            x,y = pygame.mouse.get_pos()
                            screen.blit(mouse_replace,(x,y))
                            pygame.display.update()
                    if 466<=event.pos[0]<=493 and 295<=event.pos[1]<=322:
                        timer_0 = time.time()
                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    exit()
                            if time.time() >= timer_0+5:
                                break
                            screen.blit(scene_1_bg,(0,0))
                            screen.blit(block_,(0,0))
                            screen.blit(error_1,(260,210))
                            screen.blit(text_1,(120,180))
                            x,y = pygame.mouse.get_pos()
                            screen.blit(mouse_replace,(x,y))
                            pygame.display.update()
                    if 466<=event.pos[0]<=493 and 383<=event.pos[1]<=410:
                        buloon_1 = 1
                        break
                except:
                    pass
        if buloon_1 == 1:
            pygame.mixer.music.stop()
            break
        screen.blit(scene_1_bg,(0,0))
        x,y = pygame.mouse.get_pos()
        screen.blit(mouse_replace,(x,y))
        pygame.display.update()
        
health = 100
strength = 10
iq = 250
beauty = 0
backpack = {}
textFont_character = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',18)
text_health = textFont_character.render('生命：{0}/100'.format(health),True,(0,0,0))
text_strength = textFont_character.render('力量：{0}/100'.format(strength),True,(0,0,0))
text_iq = textFont_character.render('智商：{0}/250'.format(iq),True,(0,0,0))
text.beauty = textFont_character.render('颜值：{0}/100'.format(beauty),True,(0,0,0))

main_menu()
scene_1()