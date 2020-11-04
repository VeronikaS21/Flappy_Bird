import pygame, sys

pygame.init() #initializes pygame
screen = pygame.display.set_mode((576, 1024)) # widht and height

while True:
  # to close the game
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

  pygame.display.update()
