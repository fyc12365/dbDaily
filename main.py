import os
import pygame
import time
from pygame.locals import *
from sys import exit

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('有点儿正常的大冒险')
icon = pygame.image.load('Data/image/icon.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('Data/image/bg.png')
button_start = pygame.image.load('Data/image/start.png')
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

pygame.mixer.music.load('Data/music/scene_1_bgm.ogg')

textFont_1 = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',50)
textFont_2 = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',30)
text_1 = textFont_1.render('好好学一学数学！智商-10',True,(0,0,0))
text_money1 = textFont_2.render('你有：$1.000,000,000,000',True,(0,0,0))
text_money2 = textFont_2.render('你有：$1,000,000,000,000',True,(0,0,0))

bg = pygame.image.load('Data/image/scene_1_bg.png')

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
                    iq = iq - 10
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                exit()
                        if time.time() >= timer_0+5:
                            break
                        screen.blit(bg,(0,0))
                        screen.blit(block_,(0,0))
                        screen.blit(error_1,(260,210))
                        screen.blit(text_1,(120,180))
                        x,y = pygame.mouse.get_pos()
                        screen.blit(mouse_replace,(x,y))
                        pygame.display.update()
                if 136<=event.pos[0]<=160 and 317<=event.pos[1]<=341:
                    timer_0 = time.time()
                    iq = iq - 10
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                exit()
                        if time.time() >= timer_0+5:
                            break
                        screen.blit(bg,(0,0))
                        screen.blit(block_,(0,0))
                        screen.blit(error_1,(260,210))
                        screen.blit(text_1,(120,180))
                        x,y = pygame.mouse.get_pos()
                        screen.blit(mouse_replace,(x,y))
                        pygame.display.update()
                if 136<=event.pos[0]<=160 and 380<=event.pos[1]<=404:
                    iq = iq - 10
                    timer_0 = time.time()
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                exit()
                        if time.time() >= timer_0+5:
                            break
                        screen.blit(bg,(0,0))
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
                    timer_0 = time.time()
                    iq = iq - 10
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                exit()
                        if time.time() >= timer_0+5:
                            break
                        screen.blit(bg,(0,0))
                        screen.blit(block_,(0,0))
                        screen.blit(error_1,(260,210))
                        screen.blit(text_1,(120,180))
                        x,y = pygame.mouse.get_pos()
                        screen.blit(mouse_replace,(x,y))
                        pygame.display.update()
            except:
                pass
    screen.blit(bg,(0,0))
    if buloon_2 == False:
        screen.blit(text_money1,(350,550))
    else:
        screen.blit(text_money2,(350,550))
    if buloon_1 == True:
        pygame.mixer.music.stop()
        break
    x,y = pygame.mouse.get_pos()
    screen.blit(mouse_replace,(x,y))
    pygame.display.update()

def update_health():
    global health
    if health > 100:
        health = 100
def update_strength():
    global strength
    if strength >100:
        strength = 100
def update_iq():
    global iq
    global iq_warn
    if iq > 250:
        iq = 250
        iq_warn = True
def update_beauty():
    global beauty
    global beauty_warn
    if beauty > 100:
        beauty = 100
        beauty_warn = True
def update_san():
    global san
    global san_warn
    if san > 100:
        san = 100
        san_warn = True

update_health()
update_strength()
update_iq()
update_beauty()
update_san()

text_name = textFont_character.render('姓名：李狗蛋',True,(0,0,0))
text_health = textFont_character.render('生命：{0}/100'.format(health),True,(0,0,0))
text_strength = textFont_character.render('力量：{0}/100'.format(strength),True,(0,0,0))
text_san = textFont_character.render('精神：{0}/100'.format(san),True,(0,0,0))
text_iq = textFont_character.render('智商：{0}/250'.format(iq),True,(0,0,0))
text_beauty = textFont_character.render('颜值：{0}/100'.format(beauty),True,(0,0,0))
bg = pygame.image.load('Data/image/main_bg.png')

def character_info():
    screen.blit(text_name,(10,10))
    screen.blit(text_health,(10,40))
    screen.blit(text_strength,(10,70))
    screen.blit(text_iq,(10,100))
    screen.blit(text_beauty,(10,130))
    screen.blit(text_san,(10,160))

###备忘代码行###
move_right = [pygame.image.load('actor/R1.png'),
             pygame.image.load('actor/R2.png'),
             pygame.image.load('actor/R3.png'),
             pygame.image.load('actor/R4.png'),
             pygame.image.load('actor/R5.png'),
             pygame.image.load('actor/R6.png'),
             pygame.image.load('actor/R7.png'),
             pygame.image.load('actor/R8.png'),
             pygame.image.load('actor/R9.png')]

move_left = [pygame.image.load('actor/L1.png'),
            pygame.image.load('actor/L2.png'),
            pygame.image.load('actor/L3.png'),
            pygame.image.load('actor/L4.png'),
            pygame.image.load('actor/L5.png'),
            pygame.image.load('actor/L6.png'),
            pygame.image.load('actor/L7.png'),
            pygame.image.load('actor/L8.png'),
            pygame.image.load('actor/L9.png')]

walkCount = 0
screen.blit(move_left[walkCount % 9], (x, y))
###备忘代码行###

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    screen.blit(bg,(0,0))
    character_info()
    x,y = pygame.mouse.get_pos()
    screen.blit(mouse_replace,(x,y))
    pygame.display.update()