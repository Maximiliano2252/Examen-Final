from os import system 

juegos ={
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,'IronGate']
}

inventario = {
'G001': [9990,  7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}



def validar_texto():
    texto = input("Ingrese texto")

    if texto == "":
        print("el texto no puede estar vacio")




def validar_codigo():
    codigo = input("Ingrese texto")

    if codigo =="":
        print("el texto no puede estar vacio")

    if codigo in juegos or codigo in inventario:
        print("el codigo ya existe en los datos ")

def validar_precio():
    precio = int(input("Ingrese el precio : "))
    if precio > 0:
        print("Precio ingresado correctamente...")
    else:
        print("El precio no puede ser menor o igual a 0")
    

def validar_clasificacion():
    opc = 'E','T','M'
    clasificacion = (input("Ingresa la calificacion E/T/M"))

    if clasificacion is not opc:
        print("La clasificion debe ser E,T o M ")
        return
    else: 
        print("clasificacion ingresada")
        return clasificacion
def validar_multiplayer():
    multiplayer = int(input("El juego es multiplayer? s/n : "))
    if multiplayer is 's':
        return True
    if multiplayer is 'n':
        return False
    else:
        print("opcion invalida")
        return



def validar_stock():
    stock = int(input("Ingrese stock : "))

    if stock <= 0:
        print("El stock no puede ser negativo ")
    else:
        print("Stock valido...")
def buscar_codigo(codigo) :

    codigo = (input("Ingresa el codigo : "))
    for codigo in juegos and codigo in inventario:
        print("el codigo existe..")
    else: 
        print("Codigo no encontrado")

def eliminar_juego():
    codigo_valido = buscar_codigo()

    if codigo_valido:
        juegos.remove(juegos)
        inventario.remove(codigo_valido)
        print("el juego fue eliminado..")
    else:
        ("no fue posible eliminar el juego")
def actualizar_precio():
    precio = int(input("Ingrese el precio del producto a cambiar precio :"))
    if precio in inventario:
        print("El precio fue encontrado en los juegos")
        nuevo_precio = int(input("Ingresa el precio nuevo a cambiar"))
        inventario [inventario][0] = nuevo_precio 
        return True
    else:
        print("precio no fue encontrado en el inventario")
        return False

def rango_precio(p_min,p_max):

    if p_min <= 0 and p_max <= 0:
        print("los numeros deben ser mayor que 0")


