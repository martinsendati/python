def dividir_meses(nombres_meses):
    primeros_6_meses = nombres_meses[:6]
    siguientes_6_meses = nombres_meses[6:]
    return primeros_6_meses, siguientes_6_meses

# Definir una tupla con los nombres de los meses
nombres_meses = (
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

# Llamar a la función para obtener las dos tuplas
primeros_meses, siguientes_meses = dividir_meses(nombres_meses)

# Imprimir las dos tuplas generadas
print("Primeros 6 meses:", primeros_meses)
print("Siguientes 6 meses:", siguientes_meses)

