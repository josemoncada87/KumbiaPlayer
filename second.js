const player = require('play-sound')();
const loudness = require('loudness');

// Archivos de sonido a reproducir
const soundFiles = ['./media/PistaD.mp3', './media/PistaE.mp3', './media/PistaA.mp3', './media/PistaB.mp3'];

// Volumen de cada sonido
const volumes = [50, 75, 100];
console.log(loudness.getVolume().then(
    (err, currentVolume) => {
        if (err) console.error(err);
    }
));

// Obtener el volumen actual del sistema operativo
loudness.getVolume((err, currentVolume) => {
  if (err) console.error(err);

  // Ajustar el volumen de cada sonido
  const adjustedVolumes = volumes.map(volume => {
    return Math.round(volume / 100 * currentVolume);
  });

  // Reproducir los archivos de sonido con su volumen correspondiente
  soundFiles.forEach((soundFile, i) => {
    player.play(soundFile, { afplay: ['-v', adjustedVolumes[i]] }, err => {
      if (err) console.error(err);
    });
  });
});