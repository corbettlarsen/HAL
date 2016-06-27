import pygame

class sound_board:
	def __init__(self):
	    pygame.mixer.pre_init(44100, -16, 12, 512)
    	    pygame.init()
    	    self.sound1 = pygame.mixer.Sound('sound/hal_9000.wav')
    	    self.sound2 = pygame.mixer.Sound('sound/radar.wav')
    	    self.sound3 = pygame.mixer.Sound('sound/aaaahh.wav')
    	    self.sound4 = pygame.mixer.Sound('sound/radar.wav')
    	    self.sound5 = pygame.mixer.Sound('sound/hal_9000.wav')
	def one_play(self):
	    self.sound1.play()
