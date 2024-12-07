add = lambda a, b: a + b
print(add(10, 4))

mult = lambda a, b: a * b
print(mult(10, 4))

numbers = range(11)
cuadrados = list(map(lambda x: x**2, numbers))
print(f"Cuadrados {cuadrados}")

pares = list(filter(lambda x: x%2 == 0, numbers))
print(f"Pares: {pares}")