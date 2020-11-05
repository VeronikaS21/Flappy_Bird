import pygame, sys, random # imported random to make the pipes of different sizes

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,900))
    screen.blit(floor_surface, (floor_x_pos + 576,900))

def create_pipe():
    random_pipe_positon = random.choice(pipe_height) #picks a random pipe height
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_positon))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_positon - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes       # move every pipe in the list and return the pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)  # what and position

pygame.init() #initializes pygame
screen = pygame.display.set_mode((576, 1024)) # display surface, widht and height
clock = pygame.time.Clock()

#game variables
gravity = 0.25    # to make the bird fall down
bird_movement = 0

 #Floor
bg_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/background-day.png').convert()) # to run the game faster we added convert
floor_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/base.png').convert())
floor_x_pos = 0

# Bird
bird_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/bluebird-midflap.png').convert())
bird_rect = bird_surface.get_rect(center = (100, 512))

#Pipes
pipe_surface = pygame.transform.scale2x(pygame.image.load('assets/sprites/pipe-green.png').convert())
pipe_list = [] # for making many rectangles, not just one, since we will be having many pipes that move to left
SPAWNPIPE = pygame.USEREVENT  #timer which is trigered with timer not by clicking the mouse or key
pygame.time.set_timer(SPAWNPIPE, 1200) #an event that is going to be trigered every 1.2 seconds
pipe_height = [400, 600, 800] # all the posible heights that pipes can have
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
    #pipes
      if event.type == SPAWNPIPE:
          pipe_list.extend(create_pipe())

  screen.blit(bg_surface, (0,0)) # on display surface put the background surface

  # Display the bird
  bird_movement += gravity
  bird_rect.centery += bird_movement
  screen.blit(bird_surface, bird_rect)

  # Pipes

  pipe_list = move_pipes(pipe_list)
  draw_pipes(pipe_list)
  #Floor, the image is never static it's always redrawn
  floor_x_pos -= 1
  draw_floor()
  if floor_x_pos <= -576:
      floor_x_pos = 0

  pygame.display.update()
  clock.tick(120)
