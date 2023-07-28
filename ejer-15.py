def suma_tupla(tupla):
    suma = 0
    for elemento in tupla:
        suma += elemento
    return suma

# Definir una tupla con 5 enteros
num1 = int(input("Primer numero: ")) 
num2 = int(input("Segundo numero: "))
num3 = int(input("Tercero numero: "))
num4 = int(input("Cuarto numero: "))
num5 = int(input("Quinto numero: "))

tupla_enteros = (num1, num2, num3, num4, num5)

# Calcular la suma de los elementos de la tupla
resultado = suma_tupla(tupla_enteros)

# Mostrar el resultado
print("La suma de los elementos de la tupla es:", resultado)

