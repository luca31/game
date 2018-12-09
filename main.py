import pygame, sys
from pygame.locals import *
from World import World
from Entity import Entity
from Page import Page

clock = pygame.time.Clock()

pygame.init()
size = (600,400)
screen = pygame.display.set_mode(size, (DOUBLEBUF | HWSURFACE))
pygame.display.set_caption("Painful run")

gr_player = pygame.transform.scale(pygame.image.load('images/pain_small.png'), (50,80))
player = Entity(gr_player)

gr_obstacle = pygame.transform.scale(pygame.image.load('images/itachi_small.png'), (50,60))
obstacle = Entity(gr_obstacle)

graphic = pygame.transform.scale(pygame.image.load('images/earth.png'), (80,50))
gr_cloud = pygame.transform.scale(pygame.image.load('images/cloud.png'), (80,50))

level1 = World(screen, size, graphic, gr_cloud, player, obstacle)

font = pygame.font.Font("font/CabinSketch-Bold.ttf", 50)
smallFont = pygame.font.Font("font/CabinSketch-Regular.ttf", 30)

texts = {
  "first_page": [
    [font.render('Painful Run', True, (0, 0, 0))],
    [
      smallFont.render('Press space to start', True, (0, 0, 0)),
      smallFont.render('Press i for information', True, (0, 0, 0))
    ]
  ],
  "end_page": [
    [
      font.render('Game over', True, (0, 0, 0)),
      font.render('Press space to restart', True, (0, 0, 0))
    ]
  ],
  "tutorial_page": [
    [font.render('Tutorial', True, (0, 0, 0))],
    [
      smallFont.render('You have to resist as much as possible', True, (0, 0, 0)),
      smallFont.render('You can jump by pressing space', True, (0, 0, 0)),
      smallFont.render('To go to the first page press esc', True, (0, 0, 0)),
      smallFont.render('Go back to the game by pressing esc', True, (0, 0, 0))
    ]
  ],
  "info_page": [
    [font.render('Info', True, (0, 0, 0))],
    [
      smallFont.render('Game made by:', True, (0, 0, 0)),
      smallFont.render('Luca Colli & Mattia Tagliamonte', True, (0, 0, 0)),
      smallFont.render('Press esc to go back', True, (0, 0, 0))
    ]
  ]
}

pygame.mixer.music.load("music/music.mp3")
pygame.mixer.music.queue("music/music2.mp3")
pygame.mixer.music.queue("music/music3.mp3")
pygame.mixer.music.play(-1)

def main():
  
  while level1.running == True:

    level1.moveObstacle()
    level1.moveBackground()
    level1.draw()
    if level1.checkCollision() == "end":
      level1.running = "end"
      endPage()
      break
    level1.score += 1


    if level1.up_time >= 0 and level1.up_time < 35:
      level1.playerUp()
      level1.up_time += 2
    else:
      level1.up_time = -1


    for i in pygame.event.get():
      if i.type == pygame.KEYDOWN:
        if i.key == pygame.K_SPACE and level1.up_time == -1:
          level1.up_time = 0
        if i.key == pygame.K_h:
          level1.running = "tutorial"
          tutorialPage()
          break
        if i.key == pygame.K_ESCAPE:
          level1.restart()
          level1.running = "first"
          firstPage()
          break
          
      if i.type == pygame.QUIT:
        level1.running = False
        pygame.quit()

    clock.tick(20)

first_page = Page(level1.screen)
first_page.setText(texts["first_page"][0], texts["first_page"][1])

def firstPage():
  while level1.running == "first":
    first_page.draw()

    for i in pygame.event.get():
      if i.type == pygame.KEYDOWN:
        if i.key == pygame.K_SPACE:
          level1.running = True
          main()
        if i.key == pygame.K_i:
          level1.running = "info"
          infoPage()
          break
      if i.type == pygame.QUIT:
        level1.running = False
        pygame.quit()

game_over = Page(level1.screen)

def endPage():
  while level1.running == "end":
    text_score = []
    for x in level1.str_score:
      text_score.append(smallFont.render(x, True, (0, 0, 0)))
    
    game_over.setText(texts["end_page"][0], text_score)
    game_over.draw()

    for i in pygame.event.get():
      if i.type == pygame.KEYDOWN:
        if i.key == pygame.K_SPACE:
          level1.restart()
          main()
      if i.type == pygame.QUIT:
        level1.running = False
        pygame.quit()

tutorial = Page(level1.screen)
tutorial.setText(texts["tutorial_page"][0], texts["tutorial_page"][1])

def tutorialPage():
  while level1.running == "tutorial":
    tutorial.draw()

    for i in pygame.event.get():
      if i.type == pygame.KEYDOWN:
        if i.key == pygame.K_ESCAPE:
          level1.running = True
          main()
      if i.type == pygame.QUIT:
        level1.running = False
        pygame.quit()

info = Page(level1.screen)
info.setText(texts["info_page"][0], texts["info_page"][1])

def infoPage():
  while level1.running == "info":
    info.draw()

    for i in pygame.event.get():
      if i.type == pygame.KEYDOWN:
        if i.key == pygame.K_ESCAPE:
          level1.running = "first"
          main()
      if i.type == pygame.QUIT:
        level1.running = False
        pygame.quit()

firstPage()

