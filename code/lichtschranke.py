import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
from time import sleep
import sys
import pygame

pygame.init()
effect = pygame.mixer.Sound('tor.wav')
TasterPin = 21
#Taster2Pin = 20
#GPIO.setup(Taster2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TasterPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(TasterPin) == False:
        effect.play(0)
        print('Tor unten')
	#sys.exit(0)
    #if GPIO.input(Taster2Pin) == False:
        #print('Tor unten')
        #sys.exit(0)
    else:
        print('')
sleep(0.1)
