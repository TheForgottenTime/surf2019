import pygame

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
                if(i == 11):
                    print("11")
                if(i == 4):
                    pygame.quit()


        # i = axis number
        # axes = value of the axis(i)
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
                        if (axis < 0):
                            doMovementLeft(axis)
                        elif (axis > 0):
                            doMovementRight(axis)
                    if (i == 1):
                        if (axis < 0):
                            doMovementForward(axis)
                        elif (axis > 0):
                            doMovementBackward(axis)






