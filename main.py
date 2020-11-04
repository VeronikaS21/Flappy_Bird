import pygame, sys

pygame.init() #initializes pygame
screen = pygame.display.set_mode((576, 1024)) # display surface, widht and height
clock = pygame.time.Clock()
 #added surface
bg_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/background-day.png').convert())

# Game loop
while True:
  # to close the game
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
  screen.blit(bg_surface, (0,0)) # on display surface put the background surface
  pygame.display.update()
  clock.tick(120)
