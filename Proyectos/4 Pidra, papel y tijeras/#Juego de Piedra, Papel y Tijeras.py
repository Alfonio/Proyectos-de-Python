# Juego de Piedra, Papel y Tijeras

# Importamos la librería random para hacer un random.choice() en la elección
import random

def jugar():
    opciones = ['piedra', 'papel', 'tijeras']
    
    usuario = input("Elegir: 'piedra', 'papel', 'tijeras'.\n").lower()
    
    if usuario not in opciones:
        print("¡Opción no válida! Por favor, elige entre 'piedra', 'papel' o 'tijeras'.")
        return
    
    computadora = random.choice(opciones)
    
    print(f"La computadora eligió: {computadora}")
    
    if usuario == computadora:
        return '¡Empate!'
    
    if gano_el_jugador(usuario, computadora):
        return '¡Ganaste!'
    
    return '¡Perdiste!'

# Retornar True (Verdadero) si gana el jugador.
# Piedra gana a Tijera (pi > ti).
# Tijera gana a Papel (ti > pa)
# Papel gana a Piedra (pa > pi)
def gano_el_jugador(jugador, oponente):  
    if ((jugador == 'piedra' and oponente == 'tijeras') or 
        (jugador == 'tijeras' and oponente == 'papel') or
        (jugador == 'papel' and oponente == 'piedra')):
        return True
    else:
        return False
   
print(jugar())
