import RPi.GPIO as GPIO

button_pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Estado inicial del botón (asumiendo que está en posición OFF)
button_state = GPIO.input(button_pin)

while True:
    # Detectar cambios en el estado del botón
    if GPIO.input(button_pin) != button_state:
        button_state = GPIO.input(button_pin)
        
        if button_state == GPIO.LOW:
            # El botón ha sido presionado (posición ON)
            print("Botón presionado")
        else:
            # El botón ha sido liberado (posición OFF)
            print("Botón liberado")