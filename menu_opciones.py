from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

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

    # Obtener opción del usuario
    option = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4"])

    console.print(f"Seleccionaste la opción {option}", style="bold green")

# Llamar a la función para mostrar el menú
menu()
