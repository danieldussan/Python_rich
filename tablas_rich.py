from rich.console import Console
from rich.table import Table

def show_table():
    console = Console()

    # Crear la tabla
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Nombre", style="magenta")
    table.add_column("Descripción")

    # Agregar filas a la tabla
    table.add_row("1", "Vehículo ligero", "Capacidad de hasta 0.5 toneladas")
    table.add_row("2", "Camión pesado", "Capacidad de 2.5 toneladas")
    table.add_row("3", "Vehículo particular", "Capacidad de hasta 0.6 toneladas")

    # Imprimir la tabla
    console.print(table)

# Llamar a la función para mostrar la tabla
show_table()
