import mysql.connector
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
#fromn tabla_manu_rich import * --- Con este import puedo usar las funciones del archivo tabla_menu_rich.py y las puedo usar solo con el nombre
#ejemplo imprimir_tabla(parametro)

# Conexión a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Examen_parcial"
)

def imprimir_tabla(data):
    """Imprime los datos en formato de tabla utilizando Rich."""
    console = Console()
    # Crear la tabla
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Equipo", style="magenta")
    table.add_column("Tipo", style="magenta")
    table.add_column("Placa", style="magenta")
    table.add_column("Capacidad", style="magenta")
    
    # Agregar filas a la tabla
    for row in data:
        # Convertir todos los elementos a cadenas
        row_as_str = [str(item) for item in row]
        table.add_row(*row_as_str)
    
    console.print(table)

def menu():
    console = Console()

    # Crear la tabla del menú
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Opción", width=8)
    table.add_column("Descripción")

    table.add_row("1", "Registrar un vehiculo")
    table.add_row("2", "Mostrar todos los registros")
    table.add_row("3", "Mostrar todos los tipos de vehículos cuya capacidad sea mayor o igual a 1.5 toneladas")
    table.add_row("4", "Salir")

    # Imprimir el menú
    console.print(table)

while True:
    menu()
    
    # Obtener opción del usuario usando Prompt.ask
    opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4"])

    if opcion == "1":
        # Registrar un nuevo vehículo
        mycursor = mydb.cursor()
        equipo = input("Ingrese el equipo a registrar:\n")
        tipo = input("Ingrese el tipo:\n")
        placa = input("Ingrese la placa:\n")
        capacidad = float(input("Ingrese la capacidad:\n"))  # Convertir a float
        sql = "INSERT INTO datos (equipo, tipo, placa, capacidad) VALUES (%s, %s, %s, %s)"
        values = (equipo, tipo, placa, capacidad)
        mycursor.execute(sql, values)
        mydb.commit()
        mycursor.close()
        print("Registro exitoso.")

    elif opcion == "2":
        # Mostrar todos los registros
        mycursor = mydb.cursor()
        sql = "SELECT * FROM datos"
        mycursor.execute(sql)
        response = mycursor.fetchall()
        imprimir_tabla(response)  # Pasar los datos directamente a imprimir_tabla
        mycursor.close()
        print("Datos mostrados exitosamente.")

    elif opcion == "3":
        # Mostrar vehículos con capacidad >= 1.5 toneladas
        mycursor = mydb.cursor()
        sql = "SELECT * FROM datos WHERE capacidad >= 1.5"
        mycursor.execute(sql)
        response = mycursor.fetchall()
        imprimir_tabla(response)  # Pasar los datos directamente a imprimir_tabla
        mycursor.close()
        print("Datos mostrados exitosamente.")

    elif opcion == "4":
        # Salir del programa
        print("Saliendo del programa....")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
