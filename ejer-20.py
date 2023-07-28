def contar_vocales(cadena):
    # Convertir la cadena a minúsculas para contar las vocales sin importar su caso
    cadena = cadena.lower()

    # Definir una lista con las vocales
    vocales = ['a', 'e', 'i', 'o', 'u']

    # Inicializar el contador de vocales
    contador = 0

    # Contar la cantidad de vocales en la cadena
    for letra in cadena:
        if letra in vocales:
            contador += 1

    return contador

# Ejemplo de uso
texto = input("Ingresa un texto: ")
cantidad_vocales = contar_vocales(texto)
print("La cantidad de vocales en el texto es:", cantidad_vocales)

