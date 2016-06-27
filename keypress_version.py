import random, time, pygame, sys, serial_connect, sound_board


def main():
    pygame.mixer.pre_init(44100, -16, 12, 512)
    pygame.init()
    screen = pygame.display.set_mode((320,240))
    sounds = sound_board.sound_board()
    while True:
        pygame_event = pygame.event.get()
        for event in pygame_event:
	    if event.type == pygame.KEYDOWN:
		if event.key == 113:
		    sounds.one_play()
if __name__ == '__main__':
    main()
