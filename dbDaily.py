import pygame
from sys import exit
import time
from pygame.locals import *

class character(object):
    def __init__(self,name,health,strength,iq,beauty,san):
        self.name = name
        self.health = health
        self.strength = strength
        self.iq = iq
        self.beauty = beauty
        self.san = san
        self.backpack = {}

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("有点儿正常的大冒险")
pygame.display.set_icon(pygame.image.load("Data/image/icon.png"))
