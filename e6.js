const player = require('play-sound')(opts = { player: 'mpg123' });

// Archivos de sonido a reproducir
const soundFiles = ['./media/PistaD.mp3', './media/PistaC.mp3','./media/PistaE.mp3', './media/PistaA.mp3', './media/PistaB.mp3'];
console.log(soundFiles);

// Volumen de cada pista
const volumes = [0, 0, 0, 0, 0]; // Valores de ejemplo, puedes ajustarlos según tus necesidades

// Función para reproducir una pista con un volumen específico
function playTrackWithVolume(trackIndex, volume) {
  console.log(volume, trackIndex)
  const soundFile = soundFiles[trackIndex];
  player.play(soundFile, { mpg123: ['-v', volumes[trackIndex].toString()] }, err => {
    if (err) console.error(err);
    console.log(`Reproduciendo pista ${trackIndex + 1}`);
  });
}

// Reproducir cada pista con su volumen correspondiente
soundFiles.forEach((_, i) => {
  const volume = volumes[i];
  playTrackWithVolume(i, volume);
});
