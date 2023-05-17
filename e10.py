from pygame import mixer
import pyrubberband as pyrb

# Inicializar mixer de Pygame
mixer.init()

# Cargar archivo de música en Pygame
mixer.music.load('./media/PistaE.mp3')

# Reproducir la música original
mixer.music.play()

# Crear un objeto de PyAudio para procesamiento en tiempo real
pa = pyrb.AudioProcessing()

# Establecer el tempo deseado en tiempo real
tempo_factor = 1.5  # Ejemplo: aumentar el tempo en un 50%
tempo_audio = pyrb.tempo(mixer.music.get_busy(), tempo_factor)

# Definir la función de callback para Pygame
def audio_callback(in_data, frame_count, time_info, status):
    audio_data = tempo_audio[frame_count]  # Obtener los datos de audio procesados en tiempo real
    return audio_data, pyaudio.paContinue

# Establecer la función de callback en Pygame
mixer.music.set_endevent(pygame.USEREVENT)  # Evento personalizado para el final de la reproducción
mixer.music.set_callback(audio_callback)

# Esperar a que termine la reproducción
while mixer.music.get_busy():
    pass

# Detener la reproducción y finalizar
mixer.music.stop()
mixer.quit()