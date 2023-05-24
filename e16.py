from RPi import GPIO
from time import sleep

clk = 17
dt = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                            counter += 1
                            if counter > 5:
                                counter = 5
                        else:
                            counter -= 1
                            if counter <= 0:
                                counter = 0
                        print (counter)
                clkLastState = clkState
                sleep(0.001)
finally:
        GPIO.cleanup()