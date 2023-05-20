/*const { spawn } = require('child_process');

// Archivos de sonido a reproducir
const soundFiles = ['./media/PistaD.mp3', './media/PistaC.mp3', './media/PistaE.mp3', './media/PistaA.mp3', './media/PistaB.mp3'];

soundFiles.forEach((soundFile) => {
  const player = spawn('mpg123', [soundFile]);

  player.on('error', (err) => {
    console.error(`Error al reproducir ${soundFile}: ${err.message}`);
  });

  player.on('exit', (code) => {
    if (code === 0) {
      console.log(`Reproducción de ${soundFile} finalizada exitosamente`);
    } else {
      console.error(`Error al reproducir ${soundFile}: Código de salida ${code}`);
    }
  });
});*/

const { spawn } = require('child_process');

// Archivo de sonido a reproducir
const soundFile = './media/PistaD.mp3';

// Volumen inicial
let volume = 0.5; // Valor entre 0 y 1

// Reproducir el archivo de sonido inicialmente
const player = spawn('mpg123', ['-g', volume.toString(), soundFile]);

// Función para ajustar el volumen
function setVolume(newVolume) {
  volume = newVolume;

  // Envía la señal SIGINT al proceso hijo para cambiar el volumen en tiempo de ejecución
  player.kill('SIGINT');
  player.spawn('mpg123', ['-g', volume.toString(), soundFile]);
}

// Capturar las entradas del teclado
process.stdin.setRawMode(true);
process.stdin.resume();
process.stdin.setEncoding('utf-8');

// Evento para capturar las teclas presionadas
process.stdin.on('data', (key) => {
  if (key === '+') {
    const newVolume = Math.min(volume + 0.1, 1);
    setVolume(newVolume);
  } else if (key === '-') {
    const newVolume = Math.max(volume - 0.1, 0);
    setVolume(newVolume);
  } else if (key === '\u0003') {
    // Si se presiona Ctrl+C, finalizar la reproducción y salir del programa
    player.kill();
    process.exit();
  }
});
