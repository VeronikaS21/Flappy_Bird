import pygame, sys

pygame.init() #initializes pygame
screen = pygame.display.set_mode((576, 1024)) # display surface, widht and height
clock = pygame.time.Clock()
 #added surface
bg_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/background-day.png').convert()) # to run the game faster we added convert
floor_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/base.png').convert())
floor_x_pos = 0
# Game loop
while True:
  # to close the game
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
   #background
  screen.blit(bg_surface, (0,0)) # on display surface put the background surface
  #floor, the image is never static it's always redrawn
  floor_x_pos -= 1
  screen.blit(floor_surface, (floor_x_pos,900))
  pygame.display.update()
  clock.tick(120)
