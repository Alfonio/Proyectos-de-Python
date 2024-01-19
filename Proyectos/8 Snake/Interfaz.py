#Implementacion de la biblioteca pygame y sys para salir de la pantalla
# Instalacion de la biblioteca: Pip install pygame

import pygame, sys

#Creacion del display
pygame.init()
screen = pygame.display.set_mode((1280,720)) #Tamaño interfaz
clock = pygame.time.Clock() #Frecuencia de reloj para la taza de refresco

#Creacion del loop principal
while True:
    #Dibujar los elementos
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()    
         
    pygame.display.update()
    clock.tick(60)
