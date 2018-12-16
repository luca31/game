import pygame, sys
from pygame.locals import *
pygame.init()
from World import World
from Entity import Entity
from Page import *
from texts import *
import files


def setLan(level):
  lan = files.get_data("language")
  global texts
  if lan == "I":
    texts = it
  else:
    texts = en
  level.texts = texts

clock = pygame.time.Clock()

size = (600,400)
screen = pygame.display.set_mode(size, (DOUBLEBUF | HWSURFACE))
pygame.display.set_caption("Painful run")

player = Entity("images/pain_small.png", (50,80))

obstacle = Entity("images/itachi_small.png", (50,60))

graphic = pygame.transform.scale(pygame.image.load("images/earth.png"), (80,50))
gr_cloud = pygame.transform.scale(pygame.image.load("images/cloud.png"), (80,50))

level1 = World(screen, size, graphic, gr_cloud, player, obstacle)

setLan(level1)

def setMusic():
  pygame.mixer.music.stop()
  pygame.mixer.music.load("music/music{}.mp3".format(files.get_data("soundtrack")))
  pygame.mixer.music.play(-1)

setMusic()

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


    if level1.up_time >= 0 and level1.up_time < 25:
      level1.playerUp()
      level1.up_time += 1
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


def firstPage():
  first_page = Page(level1.screen)
  first_page.setText(texts["first_page"][0], texts["first_page"][1])
  
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
        if i.key == pygame.K_s:
          level1.running = "settings"
          settingsPage()
      if i.type == pygame.QUIT:
        level1.running = False
        pygame.quit()


def endPage():
  game_over = Page(level1.screen)
  
  while level1.running == "end":
    text_score = []
    for x in level1.str_score:
      text_score.append(x)
    
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


def tutorialPage():
  tutorial = Page(level1.screen)
  tutorial.setText(texts["tutorial_page"][0], texts["tutorial_page"][1])

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


def infoPage():
  info = Page(level1.screen)
  info.setText(texts["info_page"][0], texts["info_page"][1])
  
  while level1.running == "info":
    info.draw()

    for i in pygame.event.get():
      if i.type == pygame.KEYDOWN:
        if i.key == pygame.K_ESCAPE:
          level1.running = "first"
          firstPage()
      if i.type == pygame.QUIT:
        level1.running = False
        pygame.quit()

def settingsPage():
  settings = Page(level1.screen)
  current = 1
  done = 0
  
  while level1.running == "settings":
    settings.setText(texts["settings"][0], texts["settings"][1]+texts["settings_"+str(current)+str(done)])

    settings.draw()

    for i in pygame.event.get():
      if i.type == pygame.KEYDOWN:
        if i.key == pygame.K_ESCAPE:
          level1.running = "first"
          firstPage()

        if done == 0:
          if current==1 and i.key == pygame.K_r:
            files.put_data("score", 0)
            done = 1
          if current==2 and i.key == pygame.K_1:
            files.put_data("soundtrack", 1)
            setMusic()
            done = 1
          if current==2 and i.key == pygame.K_2:
            files.put_data("soundtrack", 2)
            setMusic()
            done = 2
          if current==2 and i.key == pygame.K_3:
            files.put_data("soundtrack", 3)
            setMusic()
            done = 3
          if current==2 and i.key == pygame.K_4:
            files.put_data("soundtrack", 4)
            setMusic()
            done = 4
          if current==3 and i.key == pygame.K_e:
            files.put_data("language", "E")
            done = 1
            setLan(level1)
          if current==3 and i.key == pygame.K_i:
            files.put_data("language", "I")
            done = 1
            setLan(level1)

        if i.key == pygame.K_LEFT:
          if current > 1:
            current -= 1
          else:
            current = 3
          done = 0
        if i.key == pygame.K_RIGHT:
          if current < 3:
            current += 1
          else:
            current = 1
          done = 0
      if i.type == pygame.QUIT:
        level1.running = False
        pygame.quit()

firstPage()

