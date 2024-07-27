# pip install rich
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


# hay que pasarle una lista de tuplas
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

    # Crear la tabla del menú ENCABEZADO
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Opción", width=8)
    table.add_column("Descripción")

    # DEFINIR OPCIONES DEL MENU
    table.add_row("1", "Registrar un vehiculo")
    table.add_row("2", "Mostrar todos los registros")
    table.add_row("3", "Mostrar todos los tipos de vehículos cuya capacidad sea mayor o igual a 1.5 toneladas")
    table.add_row("4", "Salir")

    # Imprimir el menú
    console.print(table)

    # Obtener opción del usuario ----------- Las opciones tienen que ser STRINGS y al comparar tambien 
    # seran STRINGS
    option = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4"])
    console.print(f"Seleccionaste la opción {option}", style="bold green")
