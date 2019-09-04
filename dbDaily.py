import pygame
from sys import exit
import time
from pygame.locals import *

class character(object):
    def __init__(self,name,health,strength,iq,beauty,san,backpack={}):