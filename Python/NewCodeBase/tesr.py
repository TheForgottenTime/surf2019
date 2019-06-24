from gpiozero import Motor
motor1 = Motor(forward=4, backward=14)
while True:
    motor1.forward(0.5)
    sleep(5)
    motor1.reverse(0.5)
    sleep(5)