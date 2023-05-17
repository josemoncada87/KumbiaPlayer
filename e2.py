from pydub import AudioSegment
import subprocess
import time
import os

# Archivos de sonido a reproducir
sound_files = ['./media/PistaD.mp3', './media/PistaC.mp3','./media/PistaE.mp3', './media/PistaA.mp3', './media/PistaB.mp3']

# Cargar los archivos de sonido con pydub
sound_segments = [AudioSegment.from_file(sound_file) for sound_file in sound_files]

# Determinar el pitch deseado (en semitonos)
semitones = 8

# Crear un objeto subprocess para reproducir el audio en tiempo real
args = ["mpg123", "-R", "-"]
process = subprocess.Popen(args, stdin=subprocess.PIPE)

# Reproducir todos los sonidos al mismo tiempo con el pitch modificado
for sound_segment in sound_segments:
    # Cambiar el pitch del sonido
    shifted_sound = sound_segment._spawn(sound_segment.raw_data, overrides={"frame_rate": int(sound_segment.frame_rate * 2**(semitones/12))})
    # Convertir el sonido a formato mp3 y escribirlo en stdin del subprocess
    shifted_sound.export(os.path.join(os.path.dirname(__file__), 'tmp.mp3'), format="mp3")
    with open(os.path.join(os.path.dirname(__file__), 'tmp.mp3'), "rb") as f:
        data = f.read(1024)
        while data:
            process.stdin.write(data)
            data = f.read(1024)
            time.sleep(0.001)