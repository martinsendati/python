def suma_dos_mas_grandes(a, b, c):
    # Encontrar el menor valor entre a, b, y c
    min_val = min(a, b, c)

    # Sumar los dos valores más grandes excluyendo el valor mínimo
    return a + b + c - min_val

# Ejemplo de uso
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercer número entero: "))

resultado = suma_dos_mas_grandes(num1, num2, num3)
print("La suma de los dos números más grandes es:", resultado)

