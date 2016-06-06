import random, time, pygame, sys, serial_connect


def main():
    pygame.mixer.pre_init(44100, -16, 12, 512)
    pygame.init()
    sound1 = pygame.mixer.Sound('sound/hal_9000.wav')
    sound2 = pygame.mixer.Sound('sound/radar.wav')
    sound3 = pygame.mixer.Sound('sound/aaaahh.wav')
    sound4 = pygame.mixer.Sound('sound/radar.wav')
    sound5 = pygame.mixer.Sound('sound/aaaahh.wav')
    connect = serial_connect.ArduinoConnect()
    buttons = [0,0,0,0,0,0]
    while True:
        read = connect.readline()
        for i in range(5):
	    if (read & (1<<i)):
	        if (buttons[i] == 0):
		    print "playing sound" + str(i)
		    if (i == 0):
		        sound1.play()
		    if (i == 1):
			sound2.play()
		    if (i == 2):
			sound3.play()
		    if (i == 3):
			sound4.play()
		    if (i == 4):
			sound5.play()

	        buttons[i] = 1
	    else:
	        buttons[i] = 0
if __name__ == '__main__':
    main()
