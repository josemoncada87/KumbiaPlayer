import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# List of music file paths
music_files = [
    "./media/PistaB.mp3",
    "./media/PistaC.mp3",
    "./media/PistaD.mp3",
    "./media/PistaE.mp3"
    # Add more file paths as needed
]

# Play each music file in the list
for file_path in music_files:
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait until the current music file finishes playing
    while pygame.mixer.music.get_busy():
        continue

# Clean up the Pygame mixer
pygame.mixer.quit()
