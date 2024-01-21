import pygame, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.nuevo_bloque = False
        
        self.Cabeza_Ari = pygame.image.load('imagenes/Cabeza_Arriba.png').convert_alpha()
        self.Cabeza_Izq = pygame.image.load('imagenes/Cabeza_Izquierda.png').convert_alpha()
        self.Cabeza_Der = pygame.image.load('imagenes/Cabeza_Derecha.png').convert_alpha()
        self.Cabeza_Aba = pygame.image.load('imagenes/Cabeza_Abajo.png').convert_alpha()

        self.Cola_Ari = pygame.image.load('imagenes/Cola_Arriba.png').convert_alpha()
        self.Cola_Izq = pygame.image.load('imagenes/Cola_Izquierda.png').convert_alpha()
        self.Cola_Der = pygame.image.load('imagenes/Cola_Derecha.png').convert_alpha()
        self.Cola_Aba = pygame.image.load('imagenes/Cola_Abajo.png').convert_alpha()

        self.Lateral_Ari_Der = pygame.image.load('imagenes/Lateral_Arriba_Derecha.png').convert_alpha()
        self.Lateral_Ari_Izq = pygame.image.load('imagenes/Lateral_Arriba_Izquierda.png').convert_alpha()
        self.Lateral_Der = pygame.image.load('imagenes/Lateral_Derecha.png').convert_alpha()
        self.Lateral_Izq = pygame.image.load('imagenes/Lateral_Izquierda.png').convert_alpha()

        self.Centro_Hor = pygame.image.load('imagenes/Centro_Horizontal.png').convert_alpha()
        self.Centro_Ver = pygame.image.load('imagenes/Centro_Vertical.png').convert_alpha()
        


    def Dibujo_Serpiente(self):
        self.actualiza_graficos_cabeza()
        self.actualiza_graficos_Cola()
        
        for index,block in enumerate(self.body):
          #1 Todavia necesito un rectangulo para el posicionamiento
          x_pos = int(block.x * celda_tamaño)
          y_pos = int(block.y * celda_tamaño)
          block_rect = pygame.Rect(x_pos, y_pos, celda_tamaño, celda_tamaño)
          
          if index == 0:
              screen.blit(self.cabeza,block_rect)
          elif index == len(self.body) - 1:
              screen.blit(self.cola,block_rect)      
          else:
               bloque_previo = self.body[index + 1] - block
               bloque_siguiente = self.body[index - 1] - block
               
               if bloque_previo.x == bloque_siguiente.x:
                   screen.blit(self.Centro_Ver,block_rect)
                   
               elif bloque_previo.y == bloque_siguiente.y:
                   screen.blit(self.Centro_Hor,block_rect) 
                     
               else:    
                   #Son los laterales que se generan cuando cambianos en una posicion intermedia de bloque
                   if bloque_previo.x == -1 and bloque_siguiente.y == -1 or bloque_previo.y == -1 and bloque_siguiente.x == -1:
                      screen.blit(self.Lateral_Ari_Der, block_rect)
                      
                   elif bloque_previo.x == 1 and bloque_siguiente.y == -1 or bloque_previo.y == -1 and bloque_siguiente.x == 1:
                      screen.blit(self.Lateral_Ari_Izq,block_rect) 
                      
                   elif bloque_previo.x == 1 and bloque_siguiente.y == 1 or bloque_previo.y == 1 and bloque_siguiente.x == 1:
                      screen.blit(self.Lateral_Der,block_rect) 
                      
                   elif bloque_previo.x == -1 and bloque_siguiente.y == 1 or bloque_previo.y == 1 and bloque_siguiente.x == -1:
                      screen.blit(self.Lateral_Izq,block_rect)    
                                    
        #pygame.draw.rect(screen, (204, 153, 102), block_rect)   
        # for block in self.body:
        #     x_pos = int(block.x * celda_tamaño)
        #     y_pos = int(block.y * celda_tamaño)
        #     block_rect = pygame.Rect(x_pos, y_pos, celda_tamaño, celda_tamaño)
        #     pygame.draw.rect(screen, (204, 153, 102), block_rect)


    def actualiza_graficos_cabeza(self):
        
        relacion_cabeza = self.body[1] - self.body[0]
        if relacion_cabeza == Vector2(1,0): self.cabeza = self.Cabeza_Izq
        elif relacion_cabeza == Vector2(-1,0): self.cabeza = self.Cabeza_Der
        elif relacion_cabeza == Vector2(0,1): self.cabeza = self.Cabeza_Ari
        elif relacion_cabeza == Vector2(0,-1): self.cabeza = self.Cabeza_Aba
        
    
    def actualiza_graficos_Cola(self):
        
        relacion_cola = self.body[-2] - self.body[-1]
        if relacion_cola  == Vector2(1,0): self.cola = self.Cola_Der
        elif relacion_cola  == Vector2(-1,0): self.cola = self.Cola_Izq
        elif relacion_cola  == Vector2(0,1): self.cola = self.Cola_Aba
        elif relacion_cola  == Vector2(0,-1): self.cola = self.Cola_Ari    
    
    def mover_serpiente(self):
        if self.nuevo_bloque:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.nuevo_bloque = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def agregar_bloque(self):
        self.nuevo_bloque = True

class FRUTA:
    def __init__(self):
        self.Fruta_Random()

    def Dibuja_Fruta(self):
        fruta_rect = pygame.Rect(int(self.pos.x * celda_tamaño), int(self.pos.y * celda_tamaño), celda_tamaño, celda_tamaño)
        screen.blit(self.imagen, fruta_rect)

    def Fruta_Random(self):
        self.x = random.randint(0, numero_celda - 1)
        self.y = random.randint(0, numero_celda - 1)
        self.pos = Vector2(self.x, self.y)

        # Elige una imagen aleatoria y almacénala en el atributo 'imagen'
        self.imagen = random.choice(array_imagenes)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruta = FRUTA()

    def cargado(self):
        self.snake.mover_serpiente()
        self.checkear_colision()
        self.check_perdio()

    def dibuja_elementos(self):
        self.fruta.Dibuja_Fruta()
        self.snake.Dibujo_Serpiente()

    def checkear_colision(self):
        if self.fruta.pos == self.snake.body[0]:
          self.fruta.Fruta_Random()
          self.snake.agregar_bloque()

    def check_perdio(self):
        if not 0 <= self.snake.body[0].x < numero_celda or not 0 <= self.snake.body[0].y < numero_celda:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

# Creacion del display
pygame.init()
celda_tamaño = 40
numero_celda = 20
screen = pygame.display.set_mode((numero_celda * celda_tamaño, numero_celda * celda_tamaño))
clock = pygame.time.Clock()
pygame.display.set_caption("Jueguito Snake")

ima_manzana = pygame.image.load('imagenes/Manzana.png').convert_alpha()
ima_frutilla = pygame.image.load('imagenes/Frutilla.png').convert_alpha()
ima_Naranja = pygame.image.load('imagenes/Naranja.png').convert_alpha()
ima_Pera = pygame.image.load('imagenes/Pera.png').convert_alpha()
ima_Banana = pygame.image.load('imagenes/Banana.png').convert_alpha()

array_imagenes = [
    pygame.transform.scale(ima_manzana, (celda_tamaño, celda_tamaño)),
    pygame.transform.scale(ima_frutilla, (celda_tamaño, celda_tamaño)),
    pygame.transform.scale(ima_Naranja, (celda_tamaño, celda_tamaño)),
    pygame.transform.scale(ima_Pera, (celda_tamaño, celda_tamaño)),
    pygame.transform.scale(ima_Banana, (celda_tamaño, celda_tamaño)),
]

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

# Creacion del loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.cargado()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)

            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main_game.dibuja_elementos()
    pygame.display.update()
    clock.tick(10)
