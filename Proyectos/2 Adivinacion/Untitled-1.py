#Almost all module functions depend on the basic function random(), which generates a random float uniformly in the half-open range 0.0 <= X < 1.0. 
import  random
#Utilizacion de la libreria (random) para usar randint()   
def adivina_el_numero(x):
    print("__________________")
    print("!Bienvenido al Juego!")
    print("__________________")
    print("La meta es adivinar el numero generado")
    
    numero_aleatorio = random.randint(1, x) #Numero aleatorio entre 1 y x
    
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        #El usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) #Esto recibe un f-string
        
        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este numero es muy grande")  
            
    print(f"Felicidades, adivinaste el numero el cual era {numero_aleatorio}")            


adivina_el_numero(10)    