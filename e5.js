const player = require('play-sound')();
const loudness = require('loudness');

// Archivos de sonido a reproducir
const soundFiles = ['./media/PistaD.mp3', './media/PistaC.mp3','./media/PistaE.mp3', './media/PistaA.mp3', './media/PistaB.mp3'];
console.log(soundFiles);
// Volumen de cada sonido
const volumes = [0, 0, 0, 0, 0];

// Volumen general
let generalVolume = 0; // Valor de ejemplo, puedes ajustarlo según tus necesidades

soundFiles.forEach((_, i)=>{
        player.play(soundFiles[i], { generalVolume }, err => {     
            if (err) console.error(err);
        });
    });

loudness.setVolume(generalVolume);

/*
// Función para ajustar el volumen de reproducción
function setVolume(volume) {
  console.log("start", volume);
  volumes.forEach((_, i) => {
    player.play(soundFiles[i], { volume }, err => {     
      if (err) console.error(err);
    });
  });
}

// Ajustar el volumen general
loudness.setVolume(generalVolume, err => {
  console.log("set vol");
  if (err) console.error(err);
  else {
    // Ajustar el volumen de reproducción inicial
    setVolume(generalVolume);
  }
});*/
