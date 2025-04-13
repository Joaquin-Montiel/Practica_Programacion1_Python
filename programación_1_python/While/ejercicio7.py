#Guia WHILE
#Contadores - Acumuladores - Máximos y mínimos
#Ejercicio 7: Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

suma = 0
producto = 1

respuesta = "s"

while(respuesta == "s"):
    numero_entrada = int(input("Ingrese un numero: "))
    if (numero_entrada > 0):
        suma +=numero_entrada
    elif (numero_entrada < 0):
        producto *=numero_entrada

    respuesta = input("Desea continuar ingresando numeros? (s/n)")

print(f"La suma de los numeros positivos es {suma} y el producto de los negativos es {producto}.")