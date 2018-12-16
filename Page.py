import pygame

font = pygame.font.Font("font/CabinSketch-Bold.ttf", 45)
smallFont = pygame.font.Font("font/CabinSketch-Regular.ttf", 30)

class Page:
  def __init__(self, screen):
    self.screen = screen
  def setText(self, titles=[], others=[]):
    self.text = []
    self.space = 50
    for x in titles:
      self.text.append((font.render(x, True, (0, 0, 0)), (50, self.space)))
      self.space += 65
    self.space += 30
    for x in others:
      self.text.append((smallFont.render(x, True, (0, 0, 0)), (50, self.space)))
      self.space += 50  
  def draw(self):
    self.screen.fill((255,255,255))
    for x in self.text:
      self.screen.blit(x[0], x[1])
    pygame.display.update()