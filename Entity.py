import pygame, sys

class Entity:
  def __init__(self, img, size):
    self.graphic = pygame.transform.scale(pygame.image.load(img), size)
    self.size = size
    self.coords = [0,0]