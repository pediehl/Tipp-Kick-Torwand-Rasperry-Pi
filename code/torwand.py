import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
from time import sleep
import sys
import pygame

pygame.init()
effect = pygame.mixer.Sound('tor.wav')
Tor_untenPin = 21
Tor_obenPin = 20
Tor_unten = 0
Tor_oben = 0

def aktualisiereAnzeige (Tor, Punktestand):
    if Tor == "unten":
        #print (int(Punktestand / 10))
        print (Punktestand % 100)
    if Tor == "oben":
        #print (int(Punktestand / 10))
        print (Punktestand % 100)



GPIO.setup(Tor_untenPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Tor_obenPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(Tor_untenPin) == False:
        effect.play(0)
        Tor_unten = Tor_unten + 1
        aktualisiereAnzeige("unten",Tor_unten)
    if GPIO.input(Tor_obenPin) == False:
        effect.play(0)
        Tor_oben = Tor_oben + 1
        aktualisiereAnzeige("oben",Tor_unten)

sleep(0.1)
