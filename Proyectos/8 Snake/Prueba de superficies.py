#Implementacion de la biblioteca pygame y sys para salir de la pantalla
# Instalacion de la biblioteca: Pip install pygame

import pygame, sys

#Creacion del display
pygame.init()
screen = pygame.display.set_mode((1280,720)) #Tamaño interfaz
clock = pygame.time.Clock() #Frecuencia de reloj para la taza de refresco
pygame.display.set_caption("Jueguito Snake")
test_surface = pygame.Surface((100,200))
test_surface.fill("blue")
test_rect = test_surface.get_rect(center = (200,250))
#Creacion del loop principal
while True:
    #Dibujar los elementos
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
    screen.fill((175,215,70))  
    test_rect.left += 1
    screen.blit(test_surface,test_rect)         
    pygame.display.update()
    clock.tick(60)
