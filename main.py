import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,900))
    screen.blit(floor_surface, (floor_x_pos + 576,900))

pygame.init() #initializes pygame
screen = pygame.display.set_mode((576, 1024)) # display surface, widht and height
clock = pygame.time.Clock()

#game variables
gravity = 0.25    # to make the bird fall down
bird_movement = 0

 #added surface
bg_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/background-day.png').convert()) # to run the game faster we added convert
floor_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/base.png').convert())
floor_x_pos = 0
# bird surface
bird_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/bluebird-midflap.png').convert())
bird_rect = bird_surface.get_rect(center = (100, 512))
# Game loop
while True:
  # to close the game
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      if  event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
              bird_movement = 0   # to make the jump even height
              bird_movement -= 12
   #background
  screen.blit(bg_surface, (0,0)) # on display surface put the background surface

  bird_movement += gravity
  bird_rect.centery += bird_movement
  screen.blit(bird_surface, bird_rect)
  #floor, the image is never static it's always redrawn
  floor_x_pos -= 1
  draw_floor()
  if floor_x_pos <= -576:
      floor_x_pos = 0

  pygame.display.update()
  clock.tick(120)
