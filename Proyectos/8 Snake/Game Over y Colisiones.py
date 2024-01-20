import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.nuevo_bloque = False

    def Dibujo_Serpiente(self):
        for block in self.body:
            x_pos = int(block.x * celda_tamaño)
            y_pos = int(block.y * celda_tamaño)
            block_rect = pygame.Rect(x_pos, y_pos, celda_tamaño, celda_tamaño)
            pygame.draw.rect(screen, (204, 153, 102), block_rect)

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
        pygame.draw.rect(screen, (126, 166, 114), fruta_rect)

    def Fruta_Random(self):
        self.x = random.randint(0, numero_celda - 1)
        self.y = random.randint(0, numero_celda - 1)
        self.pos = Vector2(self.x, self.y)

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
