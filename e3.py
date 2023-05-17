import pygame
import pygame.mixer as mixer
import pygame.key as key

# Inicializar pygame
pygame.init()
mixer.init()

# Rutas a los archivos de audio
audio_files = ['./media/PistaD.mp3', './media/PistaE.mp3', './media/PistaA.mp3', './media/PistaB.mp3']

# Volumen inicial de cada pista de audio (valores entre 0.0 y 1.0)
volumes = [1.0, 0.5, 0.5, 1.0]

# Crear diccionario de teclas y volúmenes correspondientes
key_volumes = {pygame.K_1: 0.1, pygame.K_2: 0.3, pygame.K_3: 0.5, pygame.K_4: 0.7, pygame.K_5: 0.9}

# Cargar los archivos de audio y crear canales de mezcla
channels = []
for i, audio_file in enumerate(audio_files):
    sound = mixer.Sound(audio_file)
    sound.set_volume(volumes[i])
    channel = mixer.Channel(i)
    channels.append(channel)

# Reproducir todas las pistas al mismo tiempo
for channel in channels:
    channel.play(sound)

# Controlar el volumen de cada pista utilizando las teclas correspondientes
while True:
    # Capturar eventos del teclado
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Obtener la tecla presionada
            pressed_key = event.key

            # Comprobar si la tecla corresponde a un volumen válido
            if pressed_key in key_volumes:
                # Obtener el nuevo volumen
                new_volume = key_volumes[pressed_key]

                # Establecer el nuevo volumen en cada canal de mezcla
                for channel in channels:
                    channel.set_volume(new_volume)

        elif event.type == pygame.QUIT:
            # Salir del programa si se cierra la ventana
            pygame.quit()
            quit()
