import pygame
import random
import os

WIDTH = 640
HEIGHT = 480
FPS = 30

# ======================define colors===================
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# ===============initialize pygame and create window=========
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('a game')
clock = pygame.time.Clock()

# =========================game loop=====================
runnning = True
while running:
  	# keep loop running at the right speed
	clock.tick(FPS)
 	# process input (events)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
      	running = False
  
	  # update
  
 	 # draw / render
  	screen.fill(BLACK)
	  # after drawing everything, flip the display
  	pygame.display.flip()
  
  
pygame.quit()
