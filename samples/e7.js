const mpg = require('mpg123');
const player = new mpg.MpgPlayer();
console.log(player.channels)
player.play("D:/Usuarios/1130613425/Documents/KumbiaPlayer/media/PistaC.mp3");
console.log(player.channels)
player.volume(100);
/*
player.track - Current track name (with extention). Set to null when track completes.
player.file - Full file path, exactly as it was entered into player.play()
player.mpeg - MPEG encoding version
player.sampleRate - Track sample rate
player.channels - Number of channels
player.bitrate - Track bitrate
player.length - Track length in seconds, rounded to the nearest tenth
player.samples - Track length in raw samples
*/