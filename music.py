import random, time, pygame, sys, serial_connect
from pygame.locals import *

def main():
    
    DISPLAYSURF = pygame.display.set_mode((50, 50))
    pygame.init()
    pygame.mixer.music.load('sound/alarm.mp3')
    connect = serial_connect.ArduinoConnect()
    counter = 0
    canPlay = True
    while True:
        read = connect.readline()
##        for event in pygame.event.get():
##            if event.type == KEYDOWN:
##                pygame.mixer.music.play(-1, 0.0)
##            elif event.type == KEYUP:
##                pygame.mixer.music.stop()
##        if read:
##            canPlay = True
##        else:
##            if canPlay == True:
##                counter = counter + 1
##            if counter > 100: ##how long?
##                canPlay = False
##            if canPlay == False:
##                counter = 0
        if read:
            pygame.mixer.music.play(0, 0.0)
            
        else:
	    pygame.mixer.music.stop()
	print read
        pygame.display.update()
if __name__ == '__main__':
    main()
