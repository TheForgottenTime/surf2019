import pygame
from arduinoSerialCommunicator import writeValue

pygame.init()
pygame.joystick.init()

while True:
    
    joystick_count = pygame.joystick.get_count()

    for event in pygame.event.get():

        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        buttons = joystick.get_numbuttons()

        for i in range( buttons ):
            button = joystick.get_button( i )
            if(button):
                if(i == 12):
                    print("12")
                    writeValue("0,90,0")
                if(i == 11):
                    print("11")
                    writeValue("0,20,1")
                if(i == 4):
                    pygame.quit()


        # i = axis number
        # axes = value of the axis(i)
        axes = joystick.get_numaxes()

        for i in range( axes ):
            
            axis = joystick.get_axis( i )
            
            if (axis > -0.1 and axis < 0.1):
                axis = 0
                if (i > 3):
                    axis+=1
                    axis = axis/2
            if (abs(axis) > 0):
                
                #Changes axis values from -1 to 1 into 0-100
                axis = (axis + 1) * 50
                
                
                
                #Checking input from diffent axis
                if (i == 0):
                    if (axis < 50):
                        #doMovementLeft(axis)
                        print("left: ")
                        print(axis)
                    elif (axis > 50):
                        #doMovementRight(axis)
                        print("right: ")
                        print(axis)
                if (i == 1):
                    if (axis < 50):
                        #doMovementForward(axis)
                        print("forward: ")
                        print(axis)
                        passingString = "0," + axis + ",0"
                        writeValue(passingString)
                    elif (axis > 50):
                        #doMovementBackward(axis)
                        print("backward: ")
                        print(axis)
                        passingString = "0," + axis + ",1"
                        writeValue(passingString)







