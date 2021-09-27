import pygame
pygame.init()

pygame.mixer.music.load('audio1.mp3')


pygame.mixer.music.play()

pygame.event.wait()

print('=' * 20)
m = input()
print(f'{m}')
