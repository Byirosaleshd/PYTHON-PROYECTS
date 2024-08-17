import string
import random

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena
        
longitud = int(input("Cual es la longitud de tu contraseña deseada: ")) 

nueva_contrasena = generar_contrasena(longitud)

print("La nueva contraseña es:", nueva_contrasena)