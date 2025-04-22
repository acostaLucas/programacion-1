# Escribí un programa en Python que le pida al usuario ingresar su edad.

# Si la edad es menor a 0 o mayor a 120, mostrar un mensaje que diga: "Edad inválida".

# Si la edad es menor a 13, mostrar: "Acceso denegado. Debes tener al menos 13 años para entrar."

# Si la edad está entre 13 y 17 inclusive, mostrar: "Acceso restringido. Estás en modo adolescente."

# Si la edad es 18 o más, mostrar: "Acceso completo concedido."

import sys

edad = input("ingresa la edad: ")

try:
    edad = int(edad)
except ValueError:
    print("ingreso inválido")
    sys.exit(1)

if (edad < 13):
    print("Acceso denegado. Debes tener al menos 13 años para entrar.")
elif (edad >= 13 and edad <= 17):
    print("Acceso restringido. Estás en modo adolescente.")
elif (edad >= 18):
    print("Acceso completo concedido.")
else:
    print("Edad inválida")