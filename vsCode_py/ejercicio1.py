# Punto 1.
###################################################################################
# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el
# programa deberá determinar la posición del jugador en la cancha, considerando los
# siguientes parámetros:
#   ● Menos de 160 cm: Base
#   ● Entre 160 cm y 179 cm: Escolta
#   ● Entre 180 cm y 199 cm: Alero
#   ● 200 cm o más: Ala-Pívot o Pívot
###################################################################################

import sys

height = input(f"Ingresa la altura del jugador: ")

try:
    height = int(height)
except ValueError:
    print("Altura inválida, ingresá una altura en centímetros")
    sys.exit(1)

if height < 160:
    position = "base"
elif height >= 200:
    position = "pivot"
elif height <= 199 and height >= 180:
    position = "alero"
elif height <= 179 and height >= 160:
    position = "escolta"

print(f"Su jugador es {position.upper()}.")