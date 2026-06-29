import control_equipo as ctl

def main():
    equipos  = []
    while True:
        ctl.mostrar_menu()
        opcion = ctl.solicitar_opciones()

        if opcion == 1:
            ctl.agregar_equipo(equipos)

        elif opcion == 2:
            print("\n----BUSCAR EQUIPO----")
            busqueda = input("Ingrese el codigo del equipo. ")
            posicion = ctl.localizar_equipo(equipos, busqueda)

            if posicion != -1:
                equipo = equipos[posicion]
                print(f"\n Equipo encontrado:  {posicion}")
                print(f"codigo: {equipo['codigo']}")
                print(f"ram_gb: {equipo['ram_gb']}")
                print(f"uso_disco: {equipo['uso_disco']} ")
                print(f"requiere_mantencion: {'SI' if equipo['requiere_mantencion'] else 'NO'}")
            else:
                print(f"el equipo {busqueda} no se encuentra registrado")

        elif opcion == 3:
            print("\n-----ELIMINAR EQUIPO------")
            eliminar = input("Ingrese el codigo del equipo para eliminar. ")
            posicion = ctl.localizar_equipo(equipos, eliminar)

            if posicion != -1:
                equipos.pop(posicion)
                print(f"El equipo {eliminar} ha sido eliminado exitosamente. ")
            else:
                print(f"El equipo {eliminar} no se encuentra en el sistema.")
        
        elif opcion == 4:
            ctl.requiere_mantencion(equipos)
            print("Estados actualizados.")

        elif opcion == 5:
            ctl.requiere_mantencion(equipos)
            print("\n=====MOSTRAR EQUIPO=====")
            if not equipos:
                print("No hay equipo registrado. ")
            else:
                for equipo in equipos:
                    estado = "REQUIERE_MANTENCION" if equipo["requiere_mantencion"] else "OK"
                    print(f"codigo: {equipo['codigo']}")
                    print(f"ram_gb: {equipo['ram_gb']}")
                    print(f"uso_disco: {equipo['uso_disco']}")
                    print(f"Estado: {estado}")
                    print("*********************************************")

        elif opcion == 6:
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida, intente nuevamente.")

if __name__ == "__main__":
    main()


