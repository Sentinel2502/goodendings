import pygame
from gameObject import *
from textObject import *

pygame.init()
pygame.font.init()

class Answer(TextObject):
    def __init__(self,TextObject, value):
        self.TextObject = TextObject
        self.value = value