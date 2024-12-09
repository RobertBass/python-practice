import statistics
import csv

file_path = './files/monthly_sales.csv'
monthly_sales = {}
info = []

# LEER POR COLUMNAS
def leerProductos(path):
    with open(path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            month = row['month']
            sales =  int(row['sales'])
            monthly_sales[month] = sales
            info.append(sales)
        f.close()
    print(info)
    

def obtenerEstadisticas(data):
    # MEDIA DE LAS VENTAS
    media = statistics.mean(data)
    print(f'Media de las ventas: {media}')

    # MEDIANA DE LAS VENTAS
    mediana = statistics.median(data)
    print(f'Mediana de las ventas: {mediana}')

    # MODA DE LAS VENTAS
    moda = statistics.mode(data)
    print(f'Moda de las ventas: {moda}')

    # DESVIACION ESTANDAR
    desvStd = statistics.stdev(data)
    print(f'Desviacion Estandar de las ventas: {desvStd}')

    # VARIANZA
    varianza = statistics.variance(data)
    print(f'Varianza de las ventas: {varianza}')

    print(f'Mayor venta: {max(data)}')
    print(f'Menor venta: {min(data)}')
    print(f'Rango de ventas: {max(data) - min(data)}')



leerProductos(file_path)
obtenerEstadisticas(info)


