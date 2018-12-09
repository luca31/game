import pygame

class Page:
  def __init__(self, screen):
    self.screen = screen
  def setText(self, titles=[], others=[]):
    self.text = []
    self.space = 50
    for x in titles:
      self.text.append((x, (50, self.space)))
      self.space += 70
    self.space += 30
    for x in others:
      self.text.append((x, (50, self.space)))
      self.space += 50  
  def draw(self):
    self.screen.fill((255,255,255))
    for x in self.text:
      self.screen.blit(x[0], x[1])
    pygame.display.update()