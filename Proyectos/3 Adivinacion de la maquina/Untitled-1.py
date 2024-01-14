import random

def Computadora_adivina_el_numero(x):
    print("__________________")
    print("!Bienvenido al Juego!")
    print("__________________")
    print("La meta es adivinar el número generado")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
        # Generar predicción
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior) 
        else:
            prediccion = limite_inferior  # también podría ser limite_superior, es lo mismo
        # Obtener respuesta del usuario
        respuesta = input(f"Mi predicción de número es {prediccion}. Si es alto, ingresa (A). "
                          f"Si es bajo, ingresa (B). Si es correcto, ingresa (C) ").lower()  # el lower para que ingrese solo tome minúsculas
        
        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
            
    print(f"La computadora adivinó tu número correctamente, el cual es {prediccion}")        

Computadora_adivina_el_numero(10)
