cond1 = []
cond2 = []
empleados = [
    {
        "name": "Roberto",
        "edad": 38,
        "salary": 1000
    },
    {
        "name": "Evelyn",
        "edad": 34,
        "salary": 800
    },
    {
        "name": "Emma",
        "edad": 2,
        "salary": 500
    },
    {
        "name": "Bruno",
        "edad": 13,
        "salary": 600
    },
    {
        "name": "Emilio",
        "edad": 8,
        "salary": 700
    },
]



salario_minimo = 800
edad_minima = 12

def salario(list, validator):
    for item in list:
        if(item["salary"] >= validator):
            global cond1
            cond1.append({item["name"], item["salary"]})
    print('Proceso completado exitosamente')

def edad(list, validator):
    for item in list:
        if(item["edad"] >= validator):
            global cond2
            cond2.append({item["name"], item["edad"]})
    print('Proceso completado exitosamente')

salario(empleados, salario_minimo)
print(f'Empelados que cumplen con el salario minimo: {cond1}')
edad(empleados, edad_minima)
print(f'Empelados que cumplen con la edad minima: {cond2}')

