import pygame
from arduinoSerialCommunicator import writeValue

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

baseThrottle = 59;
currentThrottle = baseThrottle;
currentDirection = 0;
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

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
                if(i == 0):
                    currentDirection = 0;
                    toWrite = "0," + str(currentThrottle) + "," + str(currentDirection)
                    writeValue(toWrite)
                if(i == 1):
                    currentDirection = 1;
                    toWrite = "0," + str(currentThrottle) + "," + str(currentDirection)
                    writeValue(toWrite)
                if(i == 2):
                    currentThrottle -= 10;
                    toWrite = "0," + str(currentThrottle) + "," + str(currentDirection)
                    writeValue(toWrite)
                if(i == 3):
                    currentThrottle += 10;
                    toWrite = "0," + str(currentThrottle) + "," + str(currentDirection)
                    writeValue(toWrite)
                if(i == 4):
                    toWrite = "0," + str(baseThrottle) + "," + str(currentDirection)
                    writeValue(toWrite)
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
                        passingString = "0," + str(int(translate(axis, 0, 49, 1, 180))) + ",0"
                        writeValue(passingString)
                    elif (axis > 50):
                        #doMovementBackward(axis)
                        print("backward: ")
                        print(axis)
                        passingString = "0," + str(int(translate(axis, 51, 100, 1, 180))) + ",1"
                        writeValue(passingString)

    clock.tick(1)







