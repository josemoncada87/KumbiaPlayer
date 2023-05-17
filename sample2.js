const { spawn } = require('child_process');
const audioFilePath = './media/PistaD.mp3';
console.log("1");
// Comando y argumentos para ejecutar mpg123
const command = 'mpg123';
const args = ['-R', audioFilePath];
console.log("2");
// Ejecutar el comando mpg123
const player = spawn(command, args);
console.log("3");
// Manejar eventos de salida, error y cierre del proceso
player.stdout.on('data', (data) => {
  console.log(`Salida: ${data}`);
});

player.stderr.on('data', (data) => {
  console.error(`Error: ${data}`);
});

player.on('close', (code) => {
  console.log(`Proceso hijo finalizado con código de salida ${code}`);
});

//button2.watch(() => {
//  tempo += 0.1;
//  player.stdin.write(`TEMPO ${tempo}\n`);
//});

// Manejar errores y terminar la reproducción cuando finalice el archivo de sonido
player.stderr.on('data', data => {
  console.error(`stderr: ${data}`);
});

player.on('close', code => {
  console.log(`child process exited with code ${code}`);
});