# -*- coding: utf-8 -*-
import vlc
import pygame

p = vlc.MediaPlayer('Abba.mp3')
p.play()

i = 1
while not i == 0:
    p.play()
    i = int(input('digite algo para parar: '))

p.stop()

pygame.init()
pygame.mixer.music.load('Abba.mp3')
pygame.mixer.music.play()
pygame.event.wait() 