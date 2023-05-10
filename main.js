const player = require('play-sound')();
const loudness = require('loudness');

// Archivos de sonido a reproducir
const soundFiles = ['./media/PistaD.mp3', './media/PistaC.mp3','./media/PistaE.mp3', './media/PistaA.mp3', './media/PistaB.mp3'];
console.log(soundFiles);

// Volumen de cada sonido
const volumes = [0, 0, 0, 0];

soundFiles.forEach((soundFile, i) => {
    player.play(soundFile, { volume: 0 }, err => {
      if (err) console.error(err);
      console.log("play");
    });
});


//player.play('cancion.mp3', { volume: 150 }, err => {
 //   if (err) console.error(err);
 // });