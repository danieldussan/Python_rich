# Proyecto de para uso de Rich

Este proyecto es una aplicación en Python que permite registrar y consultar vehículos en una base de datos MySQL. Utiliza la biblioteca `rich` para imprimir tablas y menús con estilo en la consola.

## Requisitos

Para ejecutar este proyecto, necesitarás tener Python instalado, así como las siguientes bibliotecas:

- `mysql-connector-python`
- `rich`

Puedes instalar estas dependencias usando `pip`:

```bash
pip install mysql-connector-python rich
```

## Configuración de la Base de Datos

Asegúrate de tener una base de datos MySQL llamada `Examen_parcial` y una tabla llamada `datos` con la siguiente estructura:

```sql
CREATE TABLE datos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipo VARCHAR(255),
    tipo VARCHAR(255),
    placa VARCHAR(255),
    capacidad FLOAT
);
```

## Cómo Ejecutar

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/nombre-repositorio.git
   ```

2. **Navega al directorio del proyecto:**

   ```bash
   cd nombre-repositorio
   ```

3. **Ejecuta el script:**

   ```bash
   python main.py
   ```

## Uso

Al ejecutar el script, verás un menú con las siguientes opciones:

1. **Registrar un vehículo:** Te permite ingresar la información de un nuevo vehículo y guardarla en la base de datos.
2. **Mostrar todos los registros:** Muestra todos los registros de vehículos en la base de datos en una tabla formateada.
3. **Mostrar todos los tipos de vehículos cuya capacidad sea mayor o igual a 1.5 toneladas:** Filtra y muestra los vehículos con capacidad de 1.5 toneladas o más.
4. **Salir:** Termina la ejecución del programa.

## Explicación de `rich`

La biblioteca `rich` se utiliza para crear una salida de texto enriquecido en la consola. En este proyecto, `rich` se usa para:

- **Imprimir Tablas:** La clase `Table` de `rich` permite crear tablas con estilos personalizados para mejorar la visualización de los datos en la consola.
- **Mostrar Menús:** Se utiliza `Table` para presentar un menú claro y estilizado para el usuario.

Para más detalles sobre cómo usar `rich`, puedes consultar la [documentación oficial](https://rich.readthedocs.io/en/latest/).

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. **Haz un fork del repositorio.**
2. **Crea una nueva rama (`git checkout -b feature-nueva`).**
3. **Realiza tus cambios y haz commits (`git commit -am 'Agrega nueva funcionalidad'`).**
4. **Envía tus cambios al repositorio remoto (`git push origin feature-nueva`).**
5. **Abre una Pull Request en GitHub.**

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

Gracias por usar y contribuir a este proyecto. ¡Espero que encuentres útil esta herramienta!
