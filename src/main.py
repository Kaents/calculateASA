#main de la aplicacion para el calculo de conversion y nivel de criatura
import formulas
import convertions

# Definicion de la funcion menu para que el usuario seleccione la opcion deseada 
def menu():
    print("\nBienvenido al programa de calculo de conversion y nivel de criatura")
    print("1. Calculo de nivel de embriones")
    print("2. Calculo de conversion de tek")
    print("3. Crear nueva lista de conversiones")
    print("4. Borrar lista de conversiones")
    print("0. Salir")
    print("------------------------------------------")
    opcion = int(input("Seleccione una opcion: "))
    return opcion

def crear_nueva_lista():
    default_convertion = convertions.get_default_convertion()
    nueva_lista = {}
    print("Crea una nueva lista de conversiones personalizada.")
    print("Para saltar un item, solo presiona Enter sin escribir nada.")
    for item in default_convertion:
        entrada = input(f"Valor para '{item}' (deja vacío para omitir): ")
        if entrada.strip() == "":
            continue
        try:
            valor = int(entrada)
            nueva_lista[item] = valor
        except ValueError:
            print("Valor inválido, se omite este item.")
    nombre = input("Ponle un nombre a tu lista personalizada: ").strip()
    if not nombre:
        nombre = f"Personalizada {len(convertions.get_custom_convertions())+1}"
    convertions.add_custom_convertion(nombre, nueva_lista)
    print(f"¡Lista '{nombre}' guardada!")

def elegir_lista():
    default_convertion = convertions.get_default_convertion()
    custom_convertions = convertions.get_custom_convertions()
    print("Elige la lista de conversiones:")
    print("0. Default")
    for idx, lista in enumerate(custom_convertions, 1):
        print(f"{idx}. {lista['name']}")
    seleccion = int(input("Selecciona el número de la lista: "))
    if seleccion == 0:
        return default_convertion
    elif 1 <= seleccion <= len(custom_convertions):
        return custom_convertions[seleccion - 1]["items"]
    else:
        print("Selección inválida, usando default.")
        return default_convertion

def borrar_lista_personalizada():
    custom_convertions = convertions.get_custom_convertions()
    if not custom_convertions:
        print("No hay listas personalizadas para borrar.")
        return
    print("Listas personalizadas:")
    for idx, lista in enumerate(custom_convertions, 1):
        print(f"{idx}. {lista['name']}")
    seleccion = int(input("Selecciona el número de la lista a borrar (0 para cancelar): "))
    if 1 <= seleccion <= len(custom_convertions):
        nombre = custom_convertions[seleccion - 1]["name"]
        confirm = input(f"¿Seguro que quieres borrar '{nombre}'? (s/n): ")
        if confirm.lower() == "s":
            convertions.remove_custom_convertion(seleccion - 1)
            print(f"Lista '{nombre}' borrada.")
        else:
            print("Operación cancelada.")
    else:
        print("Operación cancelada.")

# Definicion de la funcion main para ejecutar el programa
def main():
    while True:
        opcion = menu()
        if opcion == 1:
            r = int(input("\nIngrese el nivel de la Reaper: "))
            p = int(input("Ingrese el nivel de su personaje: "))
            try:
                resultado = formulas.calculate_level(r, p)
                print("------------------------------------------")
                print(f"\nEl nivel del embrion es: {resultado}\n")
                print("------------------------------------------")
            except ValueError as e:
                print(e)
        elif opcion == 2:
            lista = elegir_lista()
            cantidad = int(input("Cantidad de tek: "))
            print("------------------------------------------")
            print(formulas.convertion_tek(cantidad, lista))
            print("------------------------------------------")
        elif opcion == 3:
            crear_nueva_lista()
        elif opcion == 4:
            borrar_lista_personalizada()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")
# Llamada a la funcion main para ejecutar el programa
if __name__ == "__main__":
    main()
# Este es el archivo principal del programa, que importa las funciones del archivo formulas.py