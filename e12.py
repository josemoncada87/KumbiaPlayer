import pygame.mixer
from threading import Thread
import os
import RPi.GPIO as GPIO

# Obtener el directorio de trabajo actual
cwd = os.getcwd()
print("Directorio de trabajo actual: {0}".format(cwd))

state1 = True
state2 = True
state3 = True
state4 = True

# Inicializar pygame.mixer
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init()

# Crear cuatro objetos de mezclador de sonido
mixer2 = pygame.mixer.Sound("./media/PistaB.ogg")
mixer3 = pygame.mixer.Sound("./media/PistaC.ogg")
mixer4 = pygame.mixer.Sound("./media/PistaD.ogg")
mixer1 = pygame.mixer.Sound("./media/PistaE.ogg")

GPIO.setmode(GPIO.BCM)
button_pins = [17, 18, 19, 20]
potentiometer_pin = 21

for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(potentiometer_pin, GPIO.IN)

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

def handle_button_press(button_number):
    if button_number == 1:
        toggle_volume(mixer1)
        print("btn1")
    elif button_number == 2:
        toggle_volume(mixer2)
        print("btn2")
    elif button_number == 3:
        toggle_volume(mixer3)
        print("btn3")
    elif button_number == 4:
        toggle_volume(mixer4)
        print("btn4")

def handle_potentiometer_change(potentiometer_value):
    global volume1, volume2, volume3, volume4
    global general_volume

    general_volume = potentiometer_value

    mixer1.set_volume(volume1 * general_volume)
    mixer2.set_volume(volume2 * general_volume)
    mixer3.set_volume(volume3 * general_volume)
    mixer4.set_volume(volume4 * general_volume)
    # ...
def toggle_volume(mixer):
    global state1, state2, state3, state4
    
    volume = 1.0

    if mixer == mixer1:
        state = state1
        volume = volume1
    elif mixer == mixer2:
        state = state2
        volume = volume2
    elif mixer == mixer3:
        state = state3
        volume = volume3
    elif mixer == mixer4:
        state = state4

    if state:
        mixer.set_volume(0.0)
    else:
        mixer.set_volume(volume * general_volume)

    if mixer == mixer1:
        state1 = not state1
    elif mixer == mixer2:
        state2 = not state2
    elif mixer == mixer3:
        state3 = not state3
    elif mixer == mixer4:
        state4 = not state4

try:
    while True:
        for i, pin in enumerate(button_pins):
            if GPIO.input(pin) == GPIO.LOW:
                handle_button_press(i + 1)
                print("Handle button", i)

        potentiometer_value = GPIO.input(potentiometer_pin)
        handle_potentiometer_change(potentiometer_value)
        
        

except KeyboardInterrupt:
    pass

