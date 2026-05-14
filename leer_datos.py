import csv
def leer_ventas(nombre_archivo): 
    try:
        with open(nombre_archivo, 'r') as archivo:
            lector_csv = csv.DictReader(archivo) #  Se crea un lector CSV que interpreta cada fila como un diccionario con claves basadas en los encabezados del archivo CSV
            ventas = [] # Lista para almacenar las ventas leídas del archivo CSV
            for fila in lector_csv:
                venta = {
                    'titulo': fila['titulo'], # Título del libro vendido
                    'genero': fila['genero'], # Género del libro vendido
                    'precio': float(fila['precio']), # Precio del libro vendido convertido a float
                    'cantidad': int(fila['cantidad']) # Cantidad de libros vendidos convertida a entero
                }
                ventas.append(venta) # Agrega la venta a la lista de ventas
            return ventas
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.") # En el caso en que el archivo no exista, se muestra un mensaje de error
        return [] 
    except Exception as e:
        print(f"Error al leer el archivo: {e}") # En el caso de que ocurra algún error durante la lectura del archivo, se muestra un mensaje de error
        return []

ventas = leer_ventas('ventas.csv')
print(ventas[0]) # Se imprime la primera venta leída del archivo CSV para verificar que se leyó correctamente.