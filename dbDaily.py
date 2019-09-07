import pygame
from sys import exit
import time
from pygame.locals import *

#定义角色类
class character(object):
    def __init__(self,name,health,strength,iq,beauty,san,pos_x=0,pos_y=0):
        self.name = name
        self.health = health
        self.strength = strength
        self.iq = iq
        self.beauty = beauty
        self.san = san
        self.backpack = {}
        self.pos_x = pos_x
        self.pos_y = pos_y
    def move_left(self):
        self.pos_x = self.pos_x - 1
        print(self.pos_x,self.pos_y)
    def move_right(self):
        self.pos_x = self.pos_x + 1
        print(self.pos_x,self.pos_y)
    def move_up(self):
        self.pos_y = self.pos_y - 1
        print(self.pos_x,self.pos_y)
    def move_down(self):
        self.pos_y = self.pos_y + 1
        print(self.pos_x,self.pos_y)

#初始化pygame及其混响（声音）
pygame.init()
pygame.mixer.init()
#创建一个800*600的窗口并设置标题、图标
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("有点儿正常的大冒险")
pygame.display.set_icon(pygame.image.load("Data/image/icon.png"))
#隐藏鼠标并加载替代图片
mouse_replace = pygame.image.load("Data/image/mouse.png")
pygame.mouse.set_visible(False)
#定义帧控制
clock = pygame.time.Clock()
#实例化角色类，角色名为LGD
LGD = character("李狗蛋",100,10,250,10,100)

'''
备忘代码行
if event.type == KEYDOWN:
    if event.key == K_UP:
        LGD.move_up()
    elif event.key == K_DOWN:
        LGD.move_down()
    elif event.key == K_LEFT:
        LGD.move_left()
    elif event.key == K_RIGHT:
        LGD.move_right()
'''

#加载图片
bg = pygame.image.load("Data/image/bg.png")
button_start = pygame.image.load("Data/image/start.png")
#一个辅助布尔值，用于一些辅助功能
buloon_0 = True
#加载音乐
pygame.mixer.music.load("Data/music/menu_bgm.ogg")
pygame.mixer.music.play(1,0)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN and 275<=event.pos[0]<=525 and 400<=event.pos[1]<=500 :
            buloon_0 = False
            pygame.mixer.music.stop()
            break
    if buloon_0 == False:
        break
    screen.blit(bg,(0,0))
    screen.blit(button_start,(275,400))
    x,y = pygame.mouse.get_pos()
    screen.blit(mouse_replace,(x,y))
    pygame.display.update()