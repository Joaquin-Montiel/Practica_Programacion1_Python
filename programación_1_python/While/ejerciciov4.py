#WHILE - Validaciones
#Ejercicio 4: Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

color ="naranja"

while (color != "azul" and color != "verde" and color != "rojo" ):
    color = input("Ingrese un color (verde/rojo/azul): ")
    if (color != "azul" and color != "verde" and color != "rojo" ):
        print("El color ingresado no es válido. Intente nuevamente.")

print(f"El color ingresado es {color}.")