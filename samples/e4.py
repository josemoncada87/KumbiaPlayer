import subprocess
import keyboard

# Rutas a los archivos de audio
audio_files = ['./media/PistaD.mp3', './media/PistaC.mp3', './media/PistaE.mp3', './media/PistaA.mp3', './media/PistaB.mp3']

# Volumen inicial de cada pista de audio (valores entre 0 y 100)
volumes = [100, 100, 100, 100, 100]

# Crear diccionario de teclas y volúmenes correspondientes
key_volumes = {keyboard.KEY_DOWN: 10, keyboard.KEY_UP: 100}

# Crear procesos para reproducir cada pista de audio
processes = []
for i, audio_file in enumerate(audio_files):
    command = ['mpg123', '-R', '--scale', str(volumes[i]), audio_file]
    process = subprocess.Popen(command)
    processes.append(process)

# Controlar el volumen de cada pista utilizando las teclas correspondientes
while True:
    try:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.scan_code in key_volumes:
            # Obtener el nuevo volumen
            new_volume = key_volumes[event.scan_code]

            # Actualizar el volumen en todos los procesos de reproducción
            for process in processes:
                process.terminate()
                command = ['mpg123', '-R', '--scale', str(new_volume), audio_file]
                process = subprocess.Popen(command)
                processes.append(process)

        elif event.event_type == keyboard.KEY_DOWN:
            print("Se presionó la tecla 'Escape'. Saliendo del programa...")
            break
    except KeyboardInterrupt:
        break

# Finalizar todos los procesos de reproducción
for process in processes:
    process.terminate()
