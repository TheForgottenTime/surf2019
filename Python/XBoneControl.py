import pygame
from Submarine import Submarine
import time


pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

thisSub = Submarine()
time.sleep(3)

goingForward = False
goingBackwards = False

while True:
    
    joystick_count = pygame.joystick.get_count()

    for event in pygame.event.get():

        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            thisSub.goStop()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        buttons = joystick.get_numbuttons()

        for i in range( buttons ):
            button = joystick.get_button( i )
            if(button):
                if(i == 0):
                    print("Going Forward")
                    thisSub.goForward(15)
                if(i == 1):
                    print("Going Backwards")
                    thisSub.goReverse(15)
                if(i == 2):
                    print("Going Left")
                    thisSub.goTurnRight()
                if(i == 3):
                    print("Going Right")
                    thisSub.goTurnRight()
                if(i == 8):
                    print("Going up")
                    thisSub.goUp()
                if(i == 4):
                    pygame.quit()


    clock.tick(1)





