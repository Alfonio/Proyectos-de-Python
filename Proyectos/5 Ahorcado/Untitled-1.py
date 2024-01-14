#importo random para tomar de la lista una palabra al azar
#importo string para tomar un todas las letras del abecedario

import random
import string
from comidas import palabras
from vidas_visuales import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
        
    return palabra.upper()

def ahorcado():
    print("__________________")
    print("!Bienvenido al Juego del Ahorcado!")
    print("__________________")
    
    palabra = obtener_palabra_valida(palabras)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    
    VIDAS = 7

    while len(letras_por_adivinar) > 0 and VIDAS > 0:
        print(f"Te quedan {VIDAS} vidas y has usado estas letras: {' '.join(letras_adivinadas)} ")
        
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        
        print(vidas_diccionario_visual[VIDAS])
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input("Escoge una letra: ").upper()
        
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            if letra_usuario in letras_por_adivinar:   
                letras_por_adivinar.discard(letra_usuario)  # Se usa discard para eliminar la letra si está presente, sin generar error si no está
                print('')
            else:
                VIDAS -= 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
            
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor, escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")
    
    if VIDAS == 0:
        print(vidas_diccionario_visual[VIDAS])
        print(f"TE AHORCARON, la palabra era: {palabra.upper()}")
    else:    
        print(f"¡Excelente, adivinaste! La palabra era {palabra.upper()}")

ahorcado()