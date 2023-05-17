import pygame
import pygame.mixer as mixer
import pygame.key as key

# Inicializar pygame
pygame.init()
mixer.init()

# Rutas a los archivos de audio
audio_files = ['./media/PistaD.mp3', './media/PistaC.mp3', './media/PistaE.mp3', './media/PistaA.mp3', './media/PistaB.mp3']

# Volumen inicial de cada pista de audio (valores entre 0.0 y 1.0)
volumes = [1.0, 1.0, 1.0, 1.0, 1.0]

# Crear diccionario de teclas y volúmenes correspondientes
key_volumes = {pygame.K_1: 0.1, pygame.K_2: 0.3, pygame.K_3: 0.5, pygame.K_4: 0.7, pygame.K_5: 0.9}

# Cargar los archivos de audio
for i, audio_file in enumerate(audio_files):
    mixer.music.load(audio_file)
    mixer.music.set_volume(volumes[i])

# Reproducir la primera pista de audio
mixer.music.play()

""" while True:
    # Capturar eventos del teclado
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.KEYDOWN:
            # Obtener la tecla presionada
            pressed_key = event.key

            # Comprobar si la tecla corresponde a un volumen válido
            if pressed_key in key_volumes:
                # Obtener el nuevo volumen
                
                new_volume = key_volumes[pressed_key]
                print(new_volume)
                # Establecer el nuevo volumen
                mixer.music.set_volume(new_volume)
                print("Volume set")
"""

import keyboard

volumeMix = 1.0

while True:
    try:
        if keyboard.is_pressed('a'):
            #print("La tecla 'a' ha sido presionada.")
            volumeMix+=1
            mixer.music.set_volume(volumeMix)            
        elif keyboard.is_pressed('b'):
            #print("La tecla 'b' ha sido presionada.")
            volumeMix-=1
            mixer.music.set_volume(volumeMix)
        elif keyboard.is_pressed('esc'):
            print("Se presionó la tecla 'Escape'. Saliendo del programa...")
            break        
    except:
        print("ERROR")
        break
