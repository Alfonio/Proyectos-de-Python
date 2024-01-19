#Importamos random para generar un rango aleatorio y el apartado de la biblioteca pygame.math para usar algunas funciones
import pygame, sys,random
from pygame.math import Vector2

#Defino una clase para la fruta donde tenga su estructura de aparicion en relacion a la posicion
class FRUTA:
    def __init__(self):
        self.x = random.randint(0,numero_celda - 1)
        self.y = random.randint(0,numero_celda - 1)
        self.pos = Vector2(self.x,self.y)
        
        
    def Dibuja_Fruta(self):
     fruta_rect = pygame.Rect(int(self.pos.x * numero_celda),int(self.pos.y * numero_celda),celda_tamaño,celda_tamaño)
     pygame.draw.rect(screen,(126,166,114),fruta_rect)    

#Creacion del display
pygame.init()
celda_tamaño = 40
numero_celda = 20
screen = pygame.display.set_mode((numero_celda * celda_tamaño,numero_celda * celda_tamaño )) #Tamaño interfaz
clock = pygame.time.Clock() #Frecuencia de reloj para la taza de refresco
pygame.display.set_caption("Jueguito Snake")

Fruta = FRUTA()

#Creacion del loop principal
while True:
    #Dibujar los elementos
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
    screen.fill((175,215,70))
    
    Fruta.Dibuja_Fruta()
            
    pygame.display.update()
    clock.tick(60)