import pygame
from sys import exit
import time
from pygame.locals import *

#定义角色类
class character(object):
    def __init__(self,name,health,strength,iq,beauty,san):
        self.name = name
        self.health = health
        self.strength = strength
        self.iq = iq
        self.beauty = beauty
        self.san = san
        self.backpack = {}
    def move_left():
        pass
    def move_right():
        pass
    def move_up():
        pass
    def move_down():
        pass

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
