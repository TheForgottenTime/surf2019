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
