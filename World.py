from random import randint
import pygame, sys
from pygame.locals import *

class World:
  def __init__(self, screen, size, graphic, gr_cloud, player, obstacle):

    self.earth = []
    for x in range(int(size[0]/80)+2):
      self.earth.append(x*80)

    self.clouds = []
    for x in range(5):
      self.clouds.append([randint(50,150)+x*90, randint(50,150)])

    player.coords[0] = size[1]/2
    obstacle.coords = [size[1]+300,0]

    self.running = True
    self.screen = screen
    self.size = size
    self.guideline = size[1]-50
    self.graphic = graphic
    self.gr_cloud = gr_cloud
    self.speed = 20
    self.player = player
    self.obstacle = obstacle

  def restart(self):
    self.running = True
    self.player.coords = [self.size[1]/2, 0]
    self.obstacle.coords = [self.size[1]+300, 0]

  def draw(self):
    screen = self.screen
    screen.fill([27, 127, 214])

    for x in self.earth:
      screen.blit(self.graphic, (x, self.guideline))
    for x in self.clouds:
      screen.blit(self.gr_cloud, x)

    font = pygame.font.Font("font/CabinSketch-Regular.ttf", 20)
    if self.score < 50:
      txt = 'Press enter to jump'
    else:
      txt = str(self.score)
    text = font.render(txt, True, (255, 255, 255))
    self.screen.blit(text, (10,10))

    screen.blit(self.player.graphic, (self.player.coords[0], self.guideline-50 - self.player.coords[1]))
    screen.blit(self.obstacle.graphic, (self.obstacle.coords[0], self.guideline-50 + 5))

    pygame.display.update()

  def playerUp(self, up_time):
    if up_time < 10:
      self.player.coords[1] += 15
    elif up_time >= 20:
      self.player.coords[1] -= 15

  def moveObstacle(self):
    if self.obstacle.coords[0] >= -50:
      self.obstacle.coords[0] -= self.speed
    else:
      self.obstacle.coords[0] = self.size[1]+300

  def moveBackground(self):
    earth = self.earth

    if earth[0] < -80:
      self.earth = [x+80 for x in earth]
    else:
      self.earth = [x-self.speed for x in earth]

    if self.score % 2 == 0:
      for x in self.clouds:
        x[0] = x[0]-1

    if self.score % 90 == 0:
      self.clouds.append([randint(50,150)+len(self.clouds)*90, randint(50,150)])

  def checkCollision(self):
    if self.player.coords[1] - self.obstacle.coords[1] < 50 and self.player.coords[0] == self.obstacle.coords[0]:
      self.running = 2

    if self.score > 150 and self.speed != 25:
      self.speed = 25


