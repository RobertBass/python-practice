nombre: str = input("Ingresa tu nombre: ")
edad: int = int(input('Ingresa tu edad: '))

def presentation(nombre: str, edad: int):
    print(f'Hola, mi nombre es {nombre}, tengo {edad} anios')


presentation(nombre, edad)
print(type(nombre))
print(type(edad))

num1: int = 20
num2: int = 5

def suma(n1: int, n2: int) -> int:
    return n1 + n2

print(suma(num1, num2))