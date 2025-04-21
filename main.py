#main de la aplicacion para el calculo de conversion y nivel de criatura
import formulas

# Definicion de la funcion menu para que el usuario seleccione la opcion deseada 
def menu():
    print("\nBienvenido al programa de calculo de conversion y nivel de criatura")
    print("1. Calculo de nivel de embriones")
    print("2. Calculo de conversion de tek")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion: "))
    return opcion

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
            quantity_tek = int(input("\nIngrese la cantidad de tek a convertir: "))
            try:
                resultado = formulas.convertion_tek(quantity_tek)
                print("\nLa conversion de tek es:")
                for item, value in resultado.items():
                    print(f"{item}: {value}")
            except ValueError as e:
                print(e)
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")
# Llamada a la funcion main para ejecutar el programa
if __name__ == "__main__":
    main()
# Este es el archivo principal del programa, que importa las funciones del archivo formulas.py