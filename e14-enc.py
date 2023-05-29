import pygame.mixer
from threading import Thread
import os
import RPi.GPIO as GPIO
import time

# Obtener el directorio de trabajo actual
cwd = os.getcwd()
print("Directorio de trabajo actual: {0}".format(cwd))

state1 = False
state2 = False
state3 = False
state4 = False

# Inicializar pygame.mixer
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init()

# Crear cuatro objetos de mezclador de sonido
mixer2 = pygame.mixer.Sound("./media/PistaB.ogg")
mixer3 = pygame.mixer.Sound("./media/PistaC.ogg")
mixer4 = pygame.mixer.Sound("./media/PistaD.ogg")
mixer1 = pygame.mixer.Sound("./media/PistaE.ogg")

GPIO.setmode(GPIO.BCM)

potentiometer_pin = 21
GPIO.setup(potentiometer_pin, GPIO.IN)

button_pins = [14, 15, 18, 20]
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


volume1 = 1.0
volume2 = 1.0
volume3 = 1.0
volume4 = 1.0

general_volume = 1.0

thread1 = Thread(target=mixer1.play)
thread2 = Thread(target=mixer2.play)
thread3 = Thread(target=mixer3.play)
thread4 = Thread(target=mixer4.play)

mixer1.play()
mixer2.play()
mixer3.play()
mixer4.play()

thread1.start()
thread2.start()
thread3.start()
thread4.start()

clk = 17
dt = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

def reportChannel():
    print(f"C1: {state1}, C2: {state2}, C3: {state3}, C4:{state4}", end="\n")

# Main program
try:
    while True:        
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
                if counter > 100:
                    counter = 100
            else:
                counter -= 1
                if counter <= 0:
                    counter = 0
            clkLastState = clkState
            clkLastState = clkState
            time.sleep(0.001)
            
            general_volume = (counter * 0.01)
            print(f"set_volume: {general_volume}")
        
        if state1:
            mixer1.set_volume(0.0)
        else:
            mixer1.set_volume(general_volume)
        
        if state2:
            mixer2.set_volume(0.0)
        else:
            mixer2.set_volume(general_volume)
            
        if state3:
            mixer3.set_volume(0.0)
        else:
            mixer3.set_volume(general_volume)
            
        if state4:
            mixer4.set_volume(0.0)
        else:
            mixer4.set_volume(general_volume)
        
        for i, pin in enumerate(button_pins):
            if i == 0:
                state1 = GPIO.input(pin)
            elif i == 1:
                state2 = GPIO.input(pin)
            elif i == 2:
                state3 = GPIO.input(pin)
            elif i == 3:
                state4 = GPIO.input(pin)

        
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    