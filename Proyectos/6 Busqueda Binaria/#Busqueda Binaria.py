# Busqueda Binaria
import random
import time

# BUSQUEDA INEFICIENTE
# Lo que hace es verificar si existe un valor en la lista igual a mi objetivo y regresar su posición del índice de ubicación
# Si mi objetivo no está en la lista, regresa un -1
def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

lista = [1, 3, 5, 10, 12]
print(busqueda_ingenua(lista, 10)) #Devuelve la posicion 3 del arreglo
print(busqueda_ingenua(lista, 7)) #Devuelve un -1 porque no se encontro en el arreglo

def búsqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Busqueda Binaria: (TIENE QUE ESTAR ORDENADA ASCENDENTE PARA QUE FUNCIONE)

def busqueda_binaria(lista, objetivo, límite_inferior=None, límite_superior=None):
    if límite_inferior is None:
        límite_inferior = 0 # Inicio de la lista
    if límite_superior is None:
        límite_superior = len(lista) - 1 # Final de la lista

    if límite_superior < límite_inferior:
        return -1

    punto_medio = (límite_inferior + límite_superior) // 2
    
    # [1, 3, 5, 10, 12]
    # 0 1  2  3  4
    # punto_medio = (0+4)//2 = 4//2 = 2
    # Esto parte la lista en el medio y busca por un lado, si no está se descarta ese espacio de lista para buscar en el otro lado de la lista
    if lista[punto_medio] == objetivo:  # Si el objetivo es el punto medio, entonces devuelve el punto medio
        return punto_medio
    elif objetivo < lista[punto_medio]:  # Si el objetivo es más chico que el punto medio, entonces se corre en 1 el punto medio para la izquierda
        return busqueda_binaria(lista, objetivo, límite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, límite_superior)
    
lista = [1, 3, 5, 10, 12]
print(busqueda_binaria(lista, 12)) #Devuelve la posicion 4 del arreglo
print(busqueda_binaria(lista, 7)) #Devuelve un -1 porque no se encontro en el arreglo


#COMPARACION DE EFICIENCIA DE LOS 2 METODOS SEGUN SU TIEMPO DE EJECUCION (IMPORT TIME)
# Crear una lista ordenada con 10000 números aleatorios.


# La construcción if __name__ == '__main__': se utiliza para asegurarse de que ciertas partes del código solo se ejecuten cuando el script se ejecuta directamente y no cuando se importa como un módulo en otro script.

if __name__ == '__main__':
    tamaño = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
     conjunto_inicial.add(random.randint(-3 * tamaño, 3 * tamaño)) # un valor aleatorio desde -30000 a 30000, es un conjunto de 60000 valores
        
    #Utilizo sorted() para ordenar la lista de menor a mayor     
    lista2 = sorted(list(conjunto_inicial)) 

    # Tiempo de ejecucion segun: Busqueda Ingenua. Tarda como 3 segundos promedio
    inicio = time.time()
    for objetivo in lista2:
        busqueda_ingenua(lista2, objetivo)
        fin = time.time()
        print(f"Tiempo de búsqueda ingenua: {fin - inicio} segundos.")

    # Tiempo de ejecucion segun: Busqueda Binaria. Tarda como 0.83 segundos promedio
    inicio = time.time()
    
    for objetivo in lista2:
        busqueda_binaria(lista2, objetivo)
        fin = time.time()
        print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos.")
        
