def mostrar_meses_y_dias():
    # Definir una tupla con los nombres de los meses
    nombres_meses = (
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    )

    # Definir una tupla con la cantidad de días de cada mes
    dias_meses = (
        31, 28, 31, 30,
        31, 30, 31, 31,
        30, 31, 30, 31
    )

    # Mostrar el contenido almacenado en las tuplas
    print("Nombres de los meses:")
    for mes in nombres_meses:
        print(mes)

    print("\nCantidad de días de cada mes:")
    for dias in dias_meses:
        print(dias)

# Llamar a la función para mostrar los meses y días
mostrar_meses_y_dias()

