from funciones import *


while True:
    print("-----Menu de opciones-----")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")

    opc = int(input("Ingrese la opcion que desea usar"))
    match=(opc)

    opc == 1
    stock_plataforma(plataforma)

    opc == 2 
    p_min= int(input("Ingrese Rango de precio minimo : "))
    p_max= int(input("Ingrese Rango de precio maximo : "))

    rango_precio(p_min,p_max)

    opc == 3
    actualizar_precio()

    opc == 4 
    codigo = validar_codigo()
    titulo = validar_texto()
    plataforma = validar_texto()
    genero = validar_texto
    clasificacion = validar_clasificacion()
    multiplayer =validar_multiplayer
    agregar_juego()

    opc == 5 
    eliminar_juego()

    opc == 6
    break
