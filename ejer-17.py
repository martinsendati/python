def contar_edades_mayores_a_20(tupla_edades):
    contador = 0
    for edad in tupla_edades:
        if edad > 20:
            contador += 1
    return contador

# Definir una tupla con 10 edades de personas
tupla_edades = (18, 25, 32, 15, 21, 28, 19, 22, 30, 27)

# Obtener la cantidad de personas con edades mayores a 20
cantidad_mayores_a_20 = contar_edades_mayores_a_20(tupla_edades)

# Imprimir el resultado
print("Cantidad de personas con edades mayores a 20:", cantidad_mayores_a_20)

