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
button_pins = [14, 15, 18, 20]
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

clk = 17
dt = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

def handle_button_press(button_number, status):
    global state1, state2, state3, state4
    
    if button_number == 1:
        state1=status
        #controlSwitch(mixer1,status)
        #print("btn1", status)
    elif button_number == 2:
        state2=status
        #controlSwitch(mixer2, status)
        #print("btn2", status)
    elif button_number == 3:
        state3=status
        #controlSwitch(mixer3, status)
        #print("btn3", status)
    elif button_number == 4:
        state4=status
        #controlSwitch(mixer4, status)
        #print("btn4", status)
    reportChannel()
    
'''def controlSwitch1(mixer, status):
    
    if mixer == mixer1:
        state1 = status
    elif mixer == mixer2:
        state2 = status
    elif mixer == mixer3:
        state3 = status
    elif mixer == mixer4:
        state4 = status
    if status:
        mixer.set_volume(1.0 * (general_volume*0.1))
    else:
        mixer.set_volume(0.0)'''

def reportChannel():
    print(f"C1: {state1}, C2: {state2}, C3: {state3}, C4:{state4}", end="\n")


# Main program
try:
    while True:
        for i, pin in enumerate(button_pins):
            handle_button_press(i + 1, GPIO.input(pin))
            time.sleep(0.2)
            '''if GPIO.input(pin) == False:
                handle_button_press(i + 1, False)
                time.sleep(0.2)
            else:
                handle_button_press(i + 1, True)
                time.sleep(0.2)'''

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
            time.sleep(0.01)
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
        
except KeyboardInterrupt:
    pass
        
finally:
        GPIO.cleanup()

'''def handle_potentiometer_change(potentiometer_value):
    global volume1, volume2, volume3, volume4
    global general_volume

    general_volume = potentiometer_value

    #mixer1.set_volume(volume1 * general_volume)
    #mixer2.set_volume(volume2 * general_volume)
    #mixer3.set_volume(volume3 * general_volume)
    #mixer4.set_volume(volume4 * general_volume)'''
    
'''def toggle_volume1(mixer):
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
        state4 = not state4 '''