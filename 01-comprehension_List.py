#COMPREHENSION LIST

# CUADRADOS
squares = [x**2 for x in range(1,11)]
print(f'Cuadrados: {squares}')


#CONVERSIONES
celsius = [0, 10, 20, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(f'Celsius to Fahrenheit: {fahrenheit}')


# NUMEROS PARES
pairs = [x for x in range(1,21) if x%2==0]
print(f'Pares: {pairs}')


# MATRIZ Y SU TRANSPUESTA
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

trans = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(trans)