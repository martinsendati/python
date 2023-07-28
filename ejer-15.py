def suma_tupla(tupla):
    suma = 0
    for elemento in tupla:
        suma += elemento
    return suma

# Definir una tupla con 5 enteros
tupla_enteros = (10, 20, 30, 40, 50)

# Calcular la suma de los elementos de la tupla
resultado = suma_tupla(tupla_enteros)

# Mostrar el resultado
print("La suma de los elementos de la tupla es:", resultado)

