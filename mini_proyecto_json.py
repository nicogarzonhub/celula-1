#El siguiente programa es ineficiente, desde que lee un archivo excel y lo transforma en JSON
import json #Importar libreria json para manipular archivos JSON
import pandas as pd #Importar pandas para manipular archivos excel

#Pasar los datos de excel a JSON (Sobrescribiendo el JSON previo)
# Cargar datos desde JSON
def cargar_datos():
    # Leer un archivo Excel
    estudiantes = {}
    try:
        df = pd.read_excel("lista_estudiantes.xlsx", sheet_name=0) #leer el archivo excel
        json_string = df.to_json()
        with open("estudiantes.json", "w") as archivo: #Se abre el JSON
            archivo.write(json_string) #Se sobrescriben los datos en el excel en el JSON
        with open("estudiantes.json", "r") as archivo:
            return json.load(archivo)
    except: #En caso de que no existan elementos dentro del excel
        return estudiantes

# Guardar datos en JSON y excel
def guardar_datos():
    try:
        with open("estudiantes.json", "w") as archivo:
            json.dump(estudiantes, archivo)
    except:
        print("Ha ocurrido un error y no se han podido guardar los datos")
#guardar un estudiante individual en el archivo de excel
def guardar_en_excel(id, nombre, edad, cedula): 
    df = pd.read_excel("lista_estudiantes.xlsx", sheet_name=0)
    df.loc[id_actual,"ID"] = id #Manera de guardar por pandas en Excel
    df.loc[id_actual,"Nombre"] = nombre
    df.loc[id_actual,"Edad"] = int(edad)
    df.loc[id_actual,"C\u00e9dula"] = cedula #Caracter \u00e9 por "é".

    df.to_excel("lista_estudiantes.xlsx", sheet_name=0, index=False)
# LISTA PRINCIPAL
estudiantes = cargar_datos()
# Calcular último ID, para sistema de ID con autoaumento
id_actual = int(max([e for e in estudiantes["ID"]], default=0))

def registrar_cedula(cedula): #Función para asegurar que la cedula ingresada no exista previamente, y por tanto, sean unicas
    try:
        cedula = int(cedula)
    except:
        return registrar_cedula(input("El valor de cedula que ha ingresado es inválido, ingrese otro: "))
    if cedula in estudiantes["C\u00e9dula"]:
        return  registrar_cedula(input("La cedula que ha ingresado ya existe, ingrese una diferente: "))
    else:
        return cedula

def registrar_estudiante(): #Función para registrar un estudiante nuevo
    global id_actual
    nombre = input("Escribe el nombre del estudiante: ")
    edad = input("Ingrese edad del estudiante: ") if nombre != "" else None
    cedula = registrar_cedula(input("Ingrese cédula del estudiante: ")) if nombre != "" else None
    while nombre != "":
        id_actual += 1
        estudiantes["ID"][id_actual] = id_actual #Manera de guardar por pandas en Excel
        estudiantes["Nombre"][id_actual] = nombre
        estudiantes["Edad"][id_actual] = edad
        estudiantes["C\u00e9dula"][id_actual] = cedula #Caracter \u00e9 por "é"
        guardar_datos() #Guardar en el JSON actual
        guardar_en_excel(id_actual, nombre, edad, cedula) #Guardar en excel
        print(" Estudiante agregado!\n")
        print("Para dejar de añadir estudiantes, presione enter sin ingresar nada")
        nombre = input("Escribe el nombre del estudiante: ")
        edad = input("Ingrese edad del estudiante: ") if nombre != "" else None
        cedula = input("Ingrese cédula del estudiante: ") if nombre != "" else None

def mostrar_estudiante():
    if len(estudiantes["ID"]) == 0:
        print("No hay estudiantes todavía\n")
    else:
        print("\n Lista de estudiantes:")
        for e in estudiantes["ID"]: #por ID en estudiantes columna ID
            print(f'ID: {e} - Nombre: {estudiantes["Nombre"][e]} - Edad: {estudiantes["Edad"][e]} - Cedula: {estudiantes["C\u00e9dula"][e]}')
        print()

# Eliminar estudiante por ID

def eliminar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes para eliminar\n")
        return

    try:
        id_buscar = int(input("Ingresa el ID del estudiante a eliminar: "))
    except:
        print("ID inválido\n")
        return
    for e in estudiantes:
        if e["id"] == id_buscar:
            estudiantes.remove(e)
            guardar_datos()
            print(" Estudiante eliminado!\n")
            return

    print("No existe un estudiante con ese ID.\n")



# Actualizar estudiante por ID

def actualizar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes para actualizar\n")
        return

    try:
        id_buscar = int(input("Ingresa el ID del estudiante a actualizar: "))
    except:
        print("ID inválido\n")
        return

    for e in estudiantes:
        if e["id"] == id_buscar:
            nuevo = input("Nuevo nombre: ")
            e["nombre"] = nuevo
            guardar_datos()
            print(" Estudiante actualizado!\n")
            return

    print(" No existe un estudiante con ese ID.\n")



# MENÚ

while True:
    print("= MENÚ PRINCIPAL =")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Eliminar estudiante")
    print("4. Actualizar estudiante")
    print("5. Salir")
  

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        mostrar_estudiante()
    elif opcion == "3":
        eliminar_estudiante()
    elif opcion == "4":
        actualizar_estudiante()
    elif opcion == "5":
        print("Gracias por usar el programa.")
        break
    else:
        print("Opción inválida\n")
