import pygame.mixer
from threading import Thread

state1 = True
state2 = True
state3 = True
state4 = True

#def play_music(file_path):
#    pygame.mixer.music.load(file_path)
#    pygame.mixer.music.play()

# Import the os module
import os
# Get the current working directory
cwd = os.getcwd()
# Print the current working directory
print("Current working directory: {0}".format(cwd))
# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))

# Inicializar pygame.mixer
pygame.mixer.init()

# Crear cuatro objetos de mezclador de sonido
mixer1 = pygame.mixer.Sound('/home/pi/KumbiaPlayer/media/PistaE.mp3')
mixer2 = pygame.mixer.Sound('/media/PistaB.mp3')
mixer3 = pygame.mixer.Sound('./media/PistaC.mp3')
mixer4 = pygame.mixer.Sound('home/pi/KumbiaPlayer/media/PistaD.mp3')

# Reproducir cada pista en un hilo separado
thread1 = Thread(target=mixer1.play)
thread2 = Thread(target=mixer2.play)
thread3 = Thread(target=mixer3.play)
thread4 = Thread(target=mixer4.play)

# Iniciar los hilos de reproducción
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Esperar a que los hilos terminen (puedes ajustar el tiempo según la duración de las pistas)
thread1.join()
thread2.join()
thread3.join()
thread4.join()

# Definir los volúmenes deseados para cada pista (valores entre 0.0 y 1.0)
volume1 = 1.0
volume2 = 1.0
volume3 = 1.0
volume4 = 1.0

# Establecer el volumen de cada pista
mixer1.set_volume(volume1)
mixer2.set_volume(volume2)
mixer3.set_volume(volume3)
mixer4.set_volume(volume4)

def reportChannel():
    print("Canal 1: ", state1)
    print("Canal 2: ", state2)
    print("Canal 3: ", state3)
    print("Canal 4: ", state4)

# Detener la reproducción al finalizar
#pygame.mixer.stop()

#Infinite loop
while True:
    print("------------------------------------------------------------------------------------")
    print("Press 'p' to pause the music")
    print("Press 'r' to resume the music")
    print("Press 'e' to exit the program")

    #take user input
    userInput = input(" ")
    
    if userInput == 'p':

        # Pause the music
        mixer1.music.pause()    
        print("music is paused....")
    elif userInput == 'r':

        # Resume the music
        mixer1.music.unpause()
        print("music is resumed....")
    elif userInput == 'e':

        # Stop the music playback
        mixer1.music.stop()
        mixer2.music.stop()
        mixer3.music.stop()
        mixer4.music.stop()
        print("music is stopped....")
        

    elif userInput == '1':
        if state1 == True:
            mixer1.set_volume(0.0)
        else:
            mixer1.set_volume(1.0)        
        state1 = not state1
        reportChannel()

    elif userInput == '2':
        if state2 == True:
            mixer2.set_volume(0.0)
        else:
            mixer2.set_volume(1.0)
        state2 = not state2
        reportChannel()

    elif userInput == '3':
        if state3 == True:
            mixer3.set_volume(0.0)
        else:
            mixer3.set_volume(1.0)
        state3 = not state3
        reportChannel()

    elif userInput == '4':
        if state4 == True:
            mixer4.set_volume(0.0)
        else:
            mixer4.set_volume(1.0)
        state4 = not state4
        reportChannel()

