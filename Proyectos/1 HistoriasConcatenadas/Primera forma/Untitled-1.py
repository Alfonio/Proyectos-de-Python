#Concatenar cadenas de caracteres para crear una historia
#Instalacion de:   pip install keyboard
#import keyboard
import keyboard

def esperar_barra_espaciadora():
    print("Presiona espacio para comenzar el siguiente quiz... ", end="", flush=True)
    keyboard.wait("space")

# Solicitar al usuario que ingrese los datos
esperar_barra_espaciadora()
print("\n")
naturaleza = input("Ingresa un entorno natural (por ejemplo, montañas): ")

nombre = input(f"{naturaleza} (Ingresa un nombre, por ejemplo, Isabella): ")
instrumento = input("Ingresa un instrumento musical (por ejemplo, piano): ")
inspiracion = input("Ingresa algo que te inspire (por ejemplo, bosque): ")
libro = input("Ingresa un objeto (por ejemplo, libro): ")
melodias = input("Ingresa algo relacionado con la música (por ejemplo, melodías): ")
piano_tipo = input("Ingresa un tipo de piano (por ejemplo, piano de cola): ")
notas_musicales = input("Ingresa algo relacionado con la música (por ejemplo, notas): ")
colores = input("Ingresa algo relacionado con colores (por ejemplo, colores brillantes): ")
sensaciones = input("Ingresa algo relacionado con sensaciones (por ejemplo, emociones): ")
comunidad = input("Ingresa algo relacionado con comunidad (por ejemplo, comunidad unida): ")
magia = input("Ingresa algo relacionado con magia (por ejemplo, magia inexplicable): ")
felicidad_emocion = input("Ingresa algo relacionado con la felicidad (por ejemplo, alegría): ")

# Crear la historia utilizando los valores ingresados por el usuario
historia_partes = [
    f"En un pequeño pueblo rodeado de {naturaleza}, vivía una joven llamada {nombre}.",
    f"Desde temprana edad, {nombre} mostró un talento excepcional para la {melodias}.",
    f"Cada día, se perdía en los sonidos de su {instrumento} en el rincón tranquilo de su hogar.",
    f"Un día, mientras exploraba el {inspiracion} cercano en busca de inspiración, {nombre} encontró un antiguo {libro} escondido entre las ramas de un viejo árbol.",
    f"El {libro} estaba lleno de {melodias} que nunca antes había escuchado. Intrigada, {nombre} decidió llevarse el {libro} a casa.",
    f"A medida que tocaba las {notas_musicales} del {libro}, algo mágico comenzó a suceder. El {instrumento} parecía cobrar vida, emitiendo una luz suave y transportando a {nombre} a un mundo lleno de {colores} y {sensaciones} inexploradas.",
    f"Cada {notas_musicales} resonaba con la esencia misma de la {felicidad_emocion}.",
    f"{nombre.capitalize()} compartió su descubrimiento con los habitantes del pueblo, y pronto la {magia} del {libro} se extendió por todo el lugar.",
    f"La {comunidad} se unió en armonía, creando una sinfonía única que llenó el aire con {felicidad_emocion} y {magia}.",
    f"Aunque {nombre} nunca entendió completamente el origen del {libro} mágico, sabía que había encontrado algo invaluable.",
    f"El pequeño pueblo, antes sumido en la monotonía, se transformó en un lugar donde la {melodias} y la creatividad florecían en cada rincón.",
    f"La historia de {nombre} y el {libro} se convirtió en leyenda, recordando a todos la magia que puede surgir de las cosas más inesperadas."
]

# Unir las partes de la historia
historia = "\n".join(historia_partes)

# Imprimir la historia generada
print("\n")
print("¡Aquí está tu historia mágica!\n")
print(historia)
 