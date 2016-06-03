import random, time, pygame, sys, serial_connect


def main():
    pygame.mixer.pre_init(44100, -16, 12, 512)
    pygame.init()
    sound1 = pygame.mixer.Sound('sound/hal_9000.wav')
    connect = serial_connect.ArduinoConnect()
    buttonPressed = 0
    while True:
        read = connect.readline()
        if read:
	    if (buttonPressed == 0):
		sound1.play()
	    buttonPressed = 1
	else:
	    buttonPressed = 0
        print read
if __name__ == '__main__':
    main()
