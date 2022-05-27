import RPi.GPIO as GPIO
import time

motorPins = (12, 16, 18, 22)
CWStep = (0x08,0x04,0x02,0x01)

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in motorPins:
        GPIO.setup(pin, GPIO.OUT)

def cycle():
    for j in range(4):
        for i in range(4):
            GPIO.output(motorPins[i], (1 << j == 1 << i) and GPIO.HIGH or GPIO.LOW)
        time.sleep(0.003)

def rotate():
    while True:
        for i in range(64):
            cycle()
        print("Cycle finished")

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print ("Cycle started")
    setup()
    try:
        rotate()
    except KeyboardInterrupt: 
        destroy()

    destroy()
