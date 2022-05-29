import RPi.GPIO as GPIO
import time

motorPins = (12, 16, 18, 22)
CWStep = (0x08,0x04,0x02,0x01)

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in motorPins:
        GPIO.setup(pin, GPIO.OUT)

def cycle(direction):
    for j in range(4):
        for i in range(4):
            GPIO.output(motorPins[i], (direction << j == direction << i) and GPIO.HIGH or GPIO.LOW)
        time.sleep(0.01)

def rotate(times, direction):
    for i in range(times * 512):
        cycle(direction)
    print("full rotation")
    time.sleep(1)

def destroy():
    GPIO.cleanup()

def start():
    times = int(input("How many rotations? "))
    direction = int(input("which directions[1 for clockwise, 4 for counterclockwise] "))
    rotate(times, direction)

if __name__ == '__main__':
    print ("Cycle started")
    setup()
    try:
        start()
    except KeyboardInterrupt: 
        destroy()

    destroy()
