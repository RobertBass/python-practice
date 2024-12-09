import csv

file_path = './files/products.csv'
updated_file_path = './files/products_updated.csv'


def agregarColumna():
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        #Obtener los nombres de las columnas existentes
        fieldnames = csv_reader.fieldnames + ['total_value']
        

        with open(updated_file_path, mode='w', newline='') as updated_file:
            csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
            csv_writer.writeheader() #Escribir los encabezados
            for row in csv_reader:
                row['total_value'] = float(row['price']) * int(row['quantity'])
                csv_writer.writerow(row)
            updated_file.close()
        file.close()


# LEER ARCHIVO
def leerCsv(path):
    with open(path, mode='r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            print(row)
    f.close()

# LEER POR COLUMNAS
def leerProductos(path):
    with open(path, mode='r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            print(f'Producto: {row['name']}, Precio: {row['price']}')
    f.close()


# INSERTAR INFO
new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accesories',
    'entry_date': '2024-12-09'
}

def agregarProducto():
    with open(file_path, mode='a+', newline='') as p:
        p.write('\n')
        csv_writer = csv.DictWriter(p, fieldnames= new_product.keys())
        csv_writer.writerow(new_product)
        print(p.read())
    p.close()


#agregarProducto()
#leerProductos()
#agregarColumna()
#leerCsv(updated_file_path)
