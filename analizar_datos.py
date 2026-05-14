from leer_datos import leer_ventas # Importa la función leer_ventas desde el módulo leer_datos para poder utilizarla en este archivo
def ingresos_por_genero(ventas):
    ingresos = {}
    for venta in ventas:
        genero = venta['genero'] # Obtiene el género del libro vendido de la venta actual
        ingreso = venta['precio'] * venta['cantidad'] # Calcula el ingreso generado por la venta multiplicando el precio del libro por la cantidad vendida
        if genero in ingresos:
            ingresos[genero] += ingreso # Si el género ya existe en el diccionario de ingresos, se suma el ingreso actual al ingreso acumulado para ese género
        else:
            ingresos[genero] = ingreso # Si el género no existe en el diccionario de ingresos, se crea una nueva entrada con el ingreso actual
    return ingresos

if __name__ == "__main__":
    ventas = leer_ventas('ventas.csv')
    print(ingresos_por_genero(ventas)) # Se llama a la función ingresos_por_genero con la lista de ventas leídas del archivo CSV y se imprime el resultado, un diccionario con los ingresos totales por género.
