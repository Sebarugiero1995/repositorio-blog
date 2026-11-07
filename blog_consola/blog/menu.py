from . import operaciones
from . import validaciones

def mostrar_menu():
    mostrar_titulo("MENÚ PRINCIPAL DEL BLOG")
    mostrar_opcion("1. Ver todos los posts")
    mostrar_opcion("2. Buscar por titulo")
    mostrar_opcion("3. Filtrar por tag")
    mostrar_opcion("4. Validar posts")
    mostrar_opcion("5. Salir")

def mostrar_titulo(titulo):
    print("\n---", titulo, "---")

def mostrar_opcion(opcion):
    print(opcion)

def elegir_opcion():
    input_opcion = input("Elegí una opción: ").strip()
    try:
        input_opcion = int(input_opcion)
        if input_opcion <= 0 or input_opcion >5:
            print("ERROR: Opción inválida. Numero elegido incorrecto")
            input_opcion = False
        if input_opcion >0 and input_opcion <6:
               return input_opcion
    except ValueError:
           print("ERROR: Opción inválida. No se puede anotar letras o símbolos")
           input_opcion = False
           
def iniciar_menu():
     while True:
                mostrar_menu()
                opcion_elegida = elegir_opcion()
                if opcion_elegida == 1:
                        operaciones.ver_posts(opcion_elegida)
                        pass
                
                if opcion_elegida == 2:
                        operaciones.buscar_titulo(opcion_elegida)
                        pass
                
                if opcion_elegida == 3:
                        operaciones.filtrar_tag(opcion_elegida)
                        pass
                
                if opcion_elegida == 4:
                        validaciones.opcion_validar_posts(opcion_elegida)
                        pass
                if opcion_elegida == 5:
                        operaciones.salir_sistema(opcion_elegida)
                        break