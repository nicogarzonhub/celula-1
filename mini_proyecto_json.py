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
        columnas = df.columns #Guardar las columnas
        arreglo = df.__array__(); #Guardar los datos pertenecientes a cada columna
        
        with open("estudiantes.json", "w") as archivo:
            json.dump(estudiantes, archivo)
    except: #En caso de que no existan elementos dentro del excel
        return estudiantes
# Guardar datos en JSON

def guardar_datos():
    with open("estudiantes.json", "w") as archivo:
        json.dump(estudiantes, archivo)
# LISTA PRINCIPAL

estudiantes = cargar_datos()

# Calcular último ID
id_actual = max([e["id"] for e in estudiantes], default=0)

# Registrar estudiante

def registrar_estudiante():
    global id_actual
    nombre = input("Escribe el nombre del estudiante: ")
    edad = input("Ingrese su edad ")
    while nombre != "":
        id_actual += 1
        estudiante = {"id": id_actual, "nombre": nombre,"edad": edad}
        
        estudiantes.append(estudiante)
        guardar_datos()
        print(" Estudiante agregado!\n")
        print("Para dejar de añadir estudiantes, presione enter sin ingresar nada")
        nombre = input("Escribe el nombre del estudiante: ")
        edad = input("Ingrese su edad ") if nombre != "" else None

def mostrar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes todavía\n")
    else:
        print("\n Lista de estudiantes:")
        for e in estudiantes:
            print(f'ID: {e["id"]} - Nombre: {e["nombre"]}')
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
