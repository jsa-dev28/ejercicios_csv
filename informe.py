from leer_datos import leer_ventas # Importa la función leer_ventas desde el módulo leer_datos para poder utilizarla en este archivo
from analizar_datos import ingresos_por_genero # Importa la función ingresos_por_genero desde el módulo analizar_datos para poder utilizarla en este archivo
def generar_informe(nombre_archivo):
    ventas = leer_ventas(nombre_archivo) # Llama a la función leer_ventas con el nombre del archivo para obtener la lista de ventas
    ingresos = ingresos_por_genero(ventas) # Llama a la función ingresos_por_genero con la lista de ventas para obtener un diccionario con los ingresos por género
    ingreso_total = sum(ingresos.values()) # Calcula el ingreso total sumando los valores del diccionario de ingresos por género
    print("Ingresos por género:")
    for genero, ingreso in ingresos.items():
        print(f"{genero}: ${ingreso}") # Imprime el género y el ingreso 
    print(f"Ingreso total: ${ingreso_total}") # Imprime el ingreso total

generar_informe('ventas.csv') # Llama a la función generar_informe con el nombre del archivo CSV para generar e imprimir el informe.
