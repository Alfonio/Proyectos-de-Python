import time
import random
from frases import frases  # Importa la lista de frases desde el archivo frases.py

border = '-+-' * 10

def caja():
    print(border)
    print('Ingresa la frase lo más rápido posible')
    print()

while True:
    # Seleccionar una frase al azar
    frase_aleatoria = random.choice(frases)
    cont_letras = len(frase_aleatoria)  # Obtén la longitud de la frase seleccionada

    t0 = time.time()
    caja()
    print(frase_aleatoria, '\n')
    inputTexto = input()
    t1 = time.time()
    long_input = len(inputTexto.split())
    aciertos = sum(1 for palabra in inputTexto.split() if palabra in frase_aleatoria.split())
    acierto = (aciertos / cont_letras) * 100
    tiempo_final = t1 - t0
    palabras_por_minuto = (long_input / tiempo_final) * 60

    # Mostrar resultados
    print('Total de palabras \t:', long_input)
    print('Tiempo usado \t:', round(tiempo_final, 2), 'segundos')
    print('Tus aciertos \t:', round(acierto, 2), '%')
    print('Velocidad es \t:', round(palabras_por_minuto, 2), 'palabras por minuto')

    print('¡QUIERES REINTENTARLO!')
    respuesta = input('Si o No \n').capitalize()
    if respuesta.lower() != 'si':
        print('¡Gracias por jugar!, Adios')
        time.sleep(1.5)
        break
