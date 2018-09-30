import pygame, sys
from pygame.locals import *
from World import World
from Entity import Entity

clock = pygame.time.Clock()

pygame.init()
size = (600,400)
screen = pygame.display.set_mode(size, (DOUBLEBUF | HWSURFACE))
pygame.display.set_caption("Painful run")

gr_player = pygame.transform.scale(pygame.image.load('images/player.png'), (30,50))
player = Entity(gr_player)

gr_obstacle = pygame.transform.scale(pygame.image.load('images/obstacle.png'), (50,50))
obstacle = Entity(gr_obstacle)

graphic = pygame.transform.scale(pygame.image.load('images/earth.png'), (80,50))
gr_cloud = pygame.transform.scale(pygame.image.load('images/cloud.png'), (80,50))

level1 = World(screen, size, graphic, gr_cloud, player, obstacle)

smallFont = pygame.font.Font("font/CabinSketch-Regular.ttf", 30)
font = pygame.font.Font("font/CabinSketch-Bold.ttf", 50)

def main():
  level1.score = 0
  up_time = -1

  while level1.running == True:
    level1.moveObstacle()
    level1.moveBackground()
    level1.draw()
    level1.checkCollision()
    level1.score += 1


    if up_time >= 0 and up_time < 30:
      level1.playerUp(up_time)
      up_time += 2
    else:
      up_time = -1


    for i in pygame.event.get():
      if i.type == pygame.KEYDOWN:
        if i.key == pygame.K_SPACE and up_time == -1:
          up_time = 0
      if i.type == pygame.QUIT:
        level1.running = False
        pygame.quit()

    clock.tick(20)


title = font.render('Painful Run', True, (0, 0, 0))
text_secondary = smallFont.render('Press space to start', True, (0, 0, 0))

while level1.running == True:
  
  level1.screen.fill((255,255,255))
  level1.screen.blit(title, (50,70))
  level1.screen.blit(text_secondary, (50,170))
  pygame.display.update()
  

  for i in pygame.event.get():
    if i.type == pygame.KEYDOWN:
      if i.key == pygame.K_SPACE:
        main()
    if i.type == pygame.QUIT:
      level1.running = False
      pygame.quit()

text_1 = font.render('Game over', True, (0, 0, 0))
text_2 = font.render('Press space to restart', True, (0, 0, 0))

while level1.running == 2:
  
  text_score = smallFont.render('Score: ' + str(level1.score), True, (0, 0, 0))

  level1.screen.fill((255,255,255))
  level1.screen.blit(text_1, (50,70))
  level1.screen.blit(text_2, (50,170))
  level1.screen.blit(text_score, (50,280))
  pygame.display.update()
  

  for i in pygame.event.get():
    if i.type == pygame.KEYDOWN:
      if i.key == pygame.K_SPACE:
        level1.restart()
        main()
    if i.type == pygame.QUIT:
      level1.running = False
      pygame.quit()
