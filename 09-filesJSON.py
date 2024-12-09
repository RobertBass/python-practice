import json

file_path = './files/products.json'
#updated_file_path = './files/products_updated.csv'

def leerJSON(path):
    with open(path, mode='r') as f:
        products = json.load(f)
    for product in products:
        print(product)
    f.close()


def leerProductos(path):
    with open(path, mode='r') as f:
        products = json.load(f)
    for product in products:
        print(f'Product: {product['name']}, Precio: {product['price']}')
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

def agregarProducto(path, product):
    with open(path, mode='r') as p:
        products = json.load(p)
        products.append(product)
        with open(path, mode='w') as f:
            json.dump(products, f, indent=4)
            f.close()
    p.close()

#leerJSON(file_path)
#leerProductos(file_path)
agregarProducto(file_path, new_product)
leerJSON(file_path)