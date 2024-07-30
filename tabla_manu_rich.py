# pip install rich
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

#pasar lista
def imprimir_tabla(data):
    """Imprime los datos en formato de tabla utilizando Rich."""
    console = Console()
    # Crear la tabla
    table = Table(show_header=True, header_style="bold blue")
    keys = list(data[0].keys())
    print(keys)
    for key in keys:
        table.add_column(key)

    # table.add_column("ID", justify="right", style="cyan")
    # table.add_column("Equipo", style="magenta")
    # table.add_column("Tipo", style="magenta")
    # table.add_column("Placa", style="magenta")
    # table.add_column("Capacidad", style="magenta")
    
    # Agregar filas a la tabla
    for row in data:
        # Convertir todos los elementos a cadenas
        print(row)
        datos = row.values()
        row_as_str = [str(item) for item in datos]
        table.add_row(*row_as_str)
    
    console.print(table)


def menu():
    console = Console()
    # Crear la tabla del menú
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Opción", width=8)
    table.add_column("Descripción")

    opciones = [
        "Registrar un vehiculo",
        "Mostrar todos los registros",
        "Mostrar todos los tipos de vehículos cuya capacidad sea mayor o igual a 1.5 toneladas",
        "Salir"        
    ]
    for count,i in enumerate(opciones):
        table.add_row(str(count+1),i)
    # ip route ip remota + ip siguiente salto
    # ipv4


    # table.add_row("1", "Registrar un vehiculo")
    # table.add_row("2", "Mostrar todos los registros")
    # table.add_row("3", "Mostrar todos los tipos de vehículos cuya capacidad sea mayor o igual a 1.5 toneladas")
    # table.add_row("4", "Salir")

    # Imprimir el menú
    console.print(table)
