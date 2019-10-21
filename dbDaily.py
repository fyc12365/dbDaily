#导入需要用到的库
import pygame
from sys import exit
import time
from pygame.locals import *

#定义角色类
class character(object):
    #基本属性
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
    #行为
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

#用一个循环保持窗口常在
while True:
    #每秒60帧
    clock.tick(60)
    #监听用户的行为
    for event in pygame.event.get():
        #点击关闭时发生QUIT事件，执行退出指令
        if event.type == QUIT:
            exit()
    #点击开始按钮后跳出此循环
        elif event.type == MOUSEBUTTONDOWN and 275<=event.pos[0]<=525 and 400<=event.pos[1]<=500 :
            buloon_0 = False
            pygame.mixer.music.stop()
            break
    if buloon_0 == False:
        pygame.mixer.music.stop()
        break
    #将背景图片和开始按钮画上去
    screen.blit(bg,(0,0))
    screen.blit(button_start,(275,400))
    #获得鼠标的坐标并将替代图片画上去
    x,y = pygame.mouse.get_pos()
    screen.blit(mouse_replace,(x,y))
    #刷新窗口（否则黑屏）
    pygame.display.update()

pygame.mixer.music.load('Data/music/scene_1_bgm.ogg')
pygame.mixer.music.play(1,0)
#加载并渲染文本
textFont_1 = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',50)
textFont_2 = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',30)
text_1 = textFont_1.render('好好学一学数学！智商-10',True,(0,0,0))
text_money1 = textFont_2.render('你有：$1.000,000,000,000',True,(0,0,0))
text_money2 = textFont_2.render('你有：$1,000,000,000,000',True,(0,0,0))

shelter_1 = pygame.image.load('Data\image\shelter_white.png')
error_1 = pygame.image.load('Data\image\error_1.jpg')
bg = pygame.image.load('Data\image\scene_1_bg.png')

def error_method1():
    time_0 = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(bg,(0,0))
        screen.blit(shelter_1,(0,0))
        screen.blit(error_1,(260,210))
        screen.blit(text_1,(120,180))
        x,y = pygame.mouse.get_pos()
        screen.blit(mouse_replace,(x,y))
        pygame.display.update()
        if time.time()>=time_0+5:
            break

buloon_1 = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
<<<<<<< HEAD
        if event.type == MOUSEBUTTONDOWN:
            if 467<=event.pos[0]<=479 and 570<=event.pos[1]<=582:
                buloon_0 = not buloon_0
            if 136<=event.pos[0]<=160 and 254<=event.pos[1]<=278:
                LGD.iq -= 10
                error_method1()
            if 136<=event.pos[0]<=160 and 317<=event.pos[1]<=341:
                LGD.iq -= 10
                error_method1()
            if 136<=event.pos[0]<=160 and 380<=event.pos[1]<=404:
                LGD.iq -= 10
                error_method1()
            if 136<=event.pos[0]<=160 and 443<=event.pos[1]<=467:
                if buloon_0 == True:
                    buloon_1 =True
                    break
                LGD.iq -= 10
                error_method1()
    if buloon_1 == True:
        pygame.mixer.music.stop()
        break
    screen.blit(bg,(0,0))
    if buloon_0 == False:
        screen.blit(text_money1,(350,550))
    else:
        screen.blit(text_money2,(350,550))
    x,y = pygame.mouse.get_pos()
    screen.blit(mouse_replace,(x,y))
    pygame.display.update()
=======
        if event.type() == MOUSEBUTTONDOWN:
            if 467<=event.pos[0]<=479 and 570<=event.pos[1]<=582:
                buloon_0 = not buloon_0
            if 136<=event.pos[0]<=160:
                if 254<=event.pos[1]<=278 or 317<=event.pos[1]<=341 or 380<=event.pos[1]<=404:
                    error_method1()
                if 443<=event.pos[1]<=467:
                    if buloon_0 = True:
                        break
                    error_method()
>>>>>>> 75f2f9989336762d0f76221730534d16e0163c6a
