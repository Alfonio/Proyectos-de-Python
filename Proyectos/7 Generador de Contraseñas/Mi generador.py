#Importo las Bibliotecas string y secrets
#String para generar constantes de caracteres predefinidas
#Secrets para la generación de números criptográficamente seguros, puedo usar random pero no es muy seguro para la seguridad de la clave

import string
import secrets

def Generador_Contraseñas(longitud, tipo):
    
    Caracteres_Contraseña = ""
    
    if tipo == 1:
        caracteres = string.ascii_letters  #ascii_letters, solo para letras
    elif tipo == 2:
        caracteres = string.ascii_letters + string.digits  #digits solo para digitos
    elif tipo == 3:
        caracteres = string.ascii_letters + string.digits + string.punctuation #punctuation para caracteres especiales
    else:
        return "Tipo de contraseña no válido" #Si el usuario ingresa un valor incorrecto

    #genero la contraseña como si fuera un random loop dentro de una lista
    contrasena = ''.join(secrets.choice(caracteres) for caracter in range(longitud))
    return contrasena

# Pide al usuario la longitud y el tipo de contraseña
longitud = int(input("Ingresa la longitud de la contraseña: "))
tipo = int(input("Selecciona el tipo de contraseña:\n"
                 "1. Solo letras\n"
                 "2. Letras y números\n"
                 "3. Letras, números y caracteres especiales\n"
                 "Ingresa el número correspondiente al tipo: "))

# Generar y mostrar la contraseña
contrasena_generada = Generador_Contraseñas(longitud, tipo)
print("Contraseña generada:", contrasena_generada)
