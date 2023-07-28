#def rango(x, y):
#   return list(range(x, y+1))

#num1 = int(input("Ingresa un número entero: "))
#num2 = int(input("Ahora otro mayor al primero: "))

#for i in rango(num1, num2):
#    print("Entre los numeros hay",  rango())

def valores_comprendidos(x, y):
    if y <= x:
        print("El segundo número debe ser mayor al primero.")
    else:
        for i in range(x + 1, y):  # Usamos range con x+1 para evitar repetir el primer número
            print(i)

# Ejemplo de uso
num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ahora otro mayor al primero: "))

valores_comprendidos(num1, num2)

