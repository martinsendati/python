def imprimir_mayores_o_iguales_a_18(tupla):
    print("Valores mayores o iguales a 18:")
    for valor in tupla:
        if valor >= 18:
            print(valor)

# Definir una tupla con 5 valores enteros
tupla_enteros = (10, 25, 8, 18, 30)

# Llamar a la función para imprimir los valores mayores o iguales a 18
imprimir_mayores_o_iguales_a_18(tupla_enteros)

