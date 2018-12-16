from random import randint
import pygame, sys
from pygame.locals import *
import files

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

    self.running = "first"
    self.screen = screen
    self.size = size
    self.guideline = size[1]-50
    self.base_color = (27, 127, 214)
    self.color = list(self.base_color)
    self.graphic = graphic
    self.gr_cloud = gr_cloud
    self.speed = 15
    self.player = player
    self.obstacle = obstacle
    self.score = 0
    self.up_time = -1

  def restart(self):
    self.running = True
    self.color = list(self.base_color)
    self.player.coords = [self.size[1]/2, 0]
    self.obstacle.coords = [self.size[1]+300, 0]
    self.speed = 15
    self.score = 0
    self.up_time = -1

  def draw(self):
    screen = self.screen
    if self.score % 15 == 0:
      for x in range(3):
        res = self.base_color[x]/100
        if self.color[x] - res >= 0:
          self.color[x] -= res
        else:
          self.color[x] = 0

    screen.fill(self.color)

    for x in self.earth:
      screen.blit(self.graphic, (x, self.guideline))
    for x in self.clouds:
      screen.blit(self.gr_cloud, x)

    font = pygame.font.Font("font/CabinSketch-Regular.ttf", 20)
    if self.score < 50:
      txt = self.texts["help"]
    else:
      txt = str(self.score)
    text = font.render(txt, True, (255, 255, 255))
    self.screen.blit(text, (10,10))

    screen.blit(self.player.graphic, (self.player.coords[0], self.guideline-80 - self.player.coords[1]))
    screen.blit(self.obstacle.graphic, (self.obstacle.coords[0], self.guideline-60))

    pygame.display.update()

  def playerUp(self):
    if self.up_time < 5:
      self.player.coords[1] += 15
    elif self.up_time >= 20:
      self.player.coords[1] -= 15

  def moveObstacle(self):
    if self.obstacle.coords[0] >= -60:
      self.obstacle.coords[0] -= self.speed
    else:
      self.obstacle.coords[0] = self.size[1] + 50*randint(4, 15)

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

  def updateScore(self):
    pre = int(files.get_data("score"))
    if self.score > pre:
      files.put_data("score", self.score)
      return 1 
    return pre

  def checkCollision(self):
    distance = (self.obstacle.size[0]+self.player.size[0])/2
    distance1 = (self.obstacle.size[1]+self.player.size[1])/2
    if -distance < self.player.coords[0] - self.obstacle.coords[0] < distance and -distance1 < self.player.coords[1] - self.obstacle.coords[1] < distance1:

      score_check = self.updateScore()

      if score_check == 1:
        self.str_score = [self.texts["score"][0].format(str(self.score))]
      else:
        self.str_score = [self.texts["score"][1].format(str(self.score)), self.texts["score"][2].format(str(score_check))]

      return "end"

    if self.score % 50 == 0:
      self.speed += 0.5


