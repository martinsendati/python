import random

def obtener_nombres_alrededor(tupla_nombres):
    # Generar un valor aleatorio entre 2 y 4 (ambos inclusive)
    valor_aleatorio = random.randint(2, 4)

    # Obtener la posición del valor aleatorio en la tupla
    posicion_aleatoria = valor_aleatorio - 1

    # Obtener los nombres de la posición aleatoria y los nombres alrededor
    nombres_alrededor = (
        tupla_nombres[posicion_aleatoria - 1],
        tupla_nombres[posicion_aleatoria],
        tupla_nombres[posicion_aleatoria + 1]
    )

    return nombres_alrededor

# Definir una tupla con 5 nombres
nombres = ("Ana", "Juan", "María", "Pedro", "Luisa")

# Llamar a la función para obtener los nombres alrededor del valor aleatorio
nombres_alrededor_aleatorio = obtener_nombres_alrededor(nombres)

# Imprimir los nombres obtenidos
print("Nombres alrededor del valor aleatorio:", nombres_alrededor_aleatorio)

