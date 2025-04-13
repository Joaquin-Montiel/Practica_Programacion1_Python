#WHILE - Validaciones
#Ejercicio Integrador: Una empresa dedicada a la toma de datos para realizar estadísticas y censos, 
# nos pide realizar la carga y validación de datos.
#Los datos requeridos son:
#Apellido
#Edad, entre 18 y 90 años inclusive.
#Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
#Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
#Una vez ingresados y validados los datos, mostrarlos por pantalla.


apellido = None
while(apellido is None or not apellido.isalpha()):
    apellido = input("Ingrese su apellido: ")
    if (not apellido.isalpha()):
        print("El apellido ingresado no es correcto. Intente nuevamente.")

edad = None
while (edad is None or edad < 18 or edad > 90):
    edad_str = input("Ingrese su edad (entre 18 y 90): ")
    edad = int(edad_str)
    if  (edad is None or edad < 18 or edad > 90):
        print("La edad ingresada no es valida. Intente nuevamente.")

estado_civil = None
while(estado_civil is None or not (estado_civil == "Soltero" or estado_civil== "Soltera" or estado_civil == "Casado" or estado_civil == "Casada" or \
                                    estado_civil == "Divorciado" or estado_civil == "Divorciada" or estado_civil == "Viuda" or estado_civil == "Viudo")):
    estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a o Viudo/a): ")
    if not ((estado_civil == "Soltero" or estado_civil== "Soltera" or estado_civil == "Casado" or estado_civil == "Casada" or \
                                    estado_civil == "Divorciado" or estado_civil == "Divorciada" or estado_civil == "Viuda" or estado_civil == "Viudo")):
        print("El estado civil ingresado no es correcto. Intente nuevamente.")

legajo = None
while(legajo is None or not (legajo.isdigit() and len(legajo) == 4 and legajo[0] != '0')):
    legajo =  input("Ingrese su numero de legajo (4 cifras sin ceros a la izquierda): ")
    if (not legajo.isdigit()):
        print("El legajo debe contener solo números.")
    elif (len(legajo) != 4):
        print("El legajo debe contener solo 4 cifras.")
    elif (len(legajo) == 4 and legajo[0] == '0'):
        print("El número del legajo no puede contener ceros a la izquierda.")

print("-----DATOS INGRESADOS-----")
print(f"APELLIDO: {apellido}.")
print(f"EDAD: {edad}.")
print(f"ESTADO CIVIL: {estado_civil}.")
print(f"LEGAJO: {legajo}.")



