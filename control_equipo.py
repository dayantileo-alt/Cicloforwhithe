def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar equipo")
    print("2. Buscar equipo")
    print("3. Eliminar equipo")
    print("4. Actualizar estados")
    print("5. Mostrar equipos")
    print("6. Salir")
    print("=====================================")

def solicitar_opciones():
    try:
        opcion = int(input("Ingrese una opcion del 1 al 6: "))
        return opcion
    except ValueError:
        return -1

def validar_codigo(nombre):
    return len (nombre.strip()) > 0

def validar_RAM(ram_gb):
    try:
        gb = int (ram_gb)
        return gb > 0
    except ValueError:
        return False

def validar_uso_disco(disco):
    try:
        uso_disco = float(disco)
        return  0.0 <= uso_disco <= 100.0
    except ValueError:
        return False
    
def agregar_equipo(lista_equipo):
    print("\n----Agregar Equipo----")
    codigo = input("Ingrese codigo del equipo: ")
    ram = input("Ingrese RAM en GB: ")
    disco = input("ingrese porcentaje de uso de disco ")

    if not validar_codigo(codigo):
        print("Error: el codigo no puede estar vacio.")
        return
    if not validar_RAM(ram):
        print("Error: la RAM debe ser en numero entero mayor a cero.")
        return
    if not validar_uso_disco(disco):
        print("Error: el uso de disco debe ser un numro decimal entre 0.0 y 100.0")
        return
    
    nuevo_equipo = {
        "codigo": codigo.strip(),
        "ram_gb": int (ram),
        "uso_disco":float(disco),
        "requiere_mantencion": False
    }
    lista_equipo.append(nuevo_equipo)
    print("Equipo agregado exitosamente.")
    
def requiere_mantencion(lista_equipo):
    for equipo in lista_equipo:
        if equipo["uso_disco"] >= 85.0:
            equipo["requiere_mantencion"] = True
        else:
            equipo["requiere_mantencion"] = False

def localizar_equipo(lista_equipo, buscar):
    for i in range(len(lista_equipo)):
        if lista_equipo[i]["codigo"].lower() == buscar.strip().lower():
            return i
    return -1

