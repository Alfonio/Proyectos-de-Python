import pygame, sys,random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        # Inicializamos el cuerpo de la serpiente con tres segmentos en posiciones específicas
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]

    def Dibujo_Serpiente(self):
        for block in self.body:
            x_pos = int(block.x * celda_tamaño)
            y_pos = int(block.y * celda_tamaño)
            # Convertir las coordenadas del bloque a píxeles en la pantalla
            block_rect = pygame.Rect(x_pos,y_pos,celda_tamaño,celda_tamaño)
             # Dibujar el bloque de la serpiente en el rectángulo
            pygame.draw.rect(screen,(255, 0, 255),block_rect)


            
#Defino una clase para la fruta donde tenga su estructura de aparicion en relacion a la posicion
class FRUTA:
    def __init__(self):
         # Inicialización de la fruta en una posición aleatoria
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

# Creación de instancias de las clases FRUTA y SNAKE
Fruta = FRUTA()
Snake = SNAKE()
#Creacion del loop principal
while True:
    #Dibujar los elementos
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
    screen.fill((175,215,70))
    
    Fruta.Dibuja_Fruta()
    Snake.Dibujo_Serpiente()        
    pygame.display.update()
    clock.tick(60)