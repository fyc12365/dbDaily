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

pygame.mixer.music.load('Data/music/menu_bgm.ogg')
pygame.mixer.music.play(1,0)
buloon_1 = False
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN and 275<=event.pos[0]<=525 and 400<=event.pos[1]<=500 :
            buloon_1 = True
            pygame.mixer.music.stop()
            break
    if buloon_1 == True:
        break
    screen.blit(bg,(0,0))
    screen.blit(button_start,(275,400))
    x, y = pygame.mouse.get_pos()
    screen.blit(mouse_replace,(x,y))
    pygame.display.update()
        
textFont_1 = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',50)
textFont_2 = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',30)
text_1 = textFont_1.render('好好学一学数学！智商-10',True,(0,0,0))
text_money1 = textFont_2.render('你有：$1.000,000,000,000',True,(0,0,0))
text_money2 = textFont_2.render('你有：$1,000,000,000,000',True,(0,0,0))

health = 100
strength = 10
iq = 250
beauty = 0
san = 98
backpack = {}
achievement = {}
iq_warn = False
beauty_warn = False
san_warn = False
textFont_character = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',18)

buloon_1 = False
buloon_2 = False
pygame.mixer.music.load('Data/music/scene_1_bgm.ogg')
pygame.mixer.music.play(1,0)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            try:
                if 136<=event.pos[0]<=160 and 254<=event.pos[1]<=278:
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
                if 136<=event.pos[0]<=160 and 317<=event.pos[1]<=341:
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
                if 136<=event.pos[0]<=160 and 380<=event.pos[1]<=404:
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
                if 467<=event.pos[0]<=479 and 570<=event.pos[1]<=582:
                    buloon_2 = not buloon_2
                if 136<=event.pos[0]<=160 and 443<=event.pos[1]<=467:
                    if buloon_2 == True:
                        buloon_1 = True
                    break
            except:
                pass
    screen.blit(scene_1_bg,(0,0))
    x,y = pygame.mouse.get_pos()
    screen.blit(mouse_replace,(x,y))
    if buloon_2 == False:
        screen.blit(text_money1,(350,550))
    else:
        screen.blit(text_money2,(350,550))
    if buloon_1 == True:
        pygame.mixer.music.stop()
        break
    pygame.display.update()

def update_health():
    if health > 100:
        health = 100
    text_health = textFont_character.render('生命：{0}/100'.format(health),True,(0,0,0))
def update_strength():
    if strength >100:
        strength = 100
    text_strength = textFont_character.render('力量：{0}/100'.format(strength),True,(0,0,0))
def update_iq():
    if iq > 250:
        iq = 250
        iq_warn = True
    text_iq = textFont_character.render('智商：{0}/250'.format(iq),True,(0,0,0))
def update_beauty():
    if beauty > 100:
        beauty = 100
        beauty_warn = True
    text_beauty = textFont_character.render('颜值：{0}/100'.format(beauty),True,(0,0,0))
def update_san():
    if san > 100:
        san = 100
        san_warn = True
    test_san = textFont_character.render('精神：{0}/100'.format(san),True,(0,0,0))

update_health()
update_strength()
update_iq()
update_beauty()
update_san()