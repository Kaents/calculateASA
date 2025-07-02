#main de la aplicacion para el calculo de conversion y nivel de criatura
import formulas
from convertions.def_list_convertions import (
    create_new_list,
    choose_list,
    delete_custom_list,
    choose_item_or_all
)
import translations.def_translations as def_translations

# Definicion de la funcion menu para que el usuario seleccione la opcion deseada 
def menu():
    print(def_translations.translate("\nWelcome to the conversion and creature level calculator.\n"))
    print(def_translations.translate("1. Embryo level calculation"))
    print(def_translations.translate("2. Tek conversion calculation"))
    print(def_translations.translate("3. Create new conversion list"))
    print(def_translations.translate("4. Delete custom conversion list"))
    print(def_translations.translate("0. Exit"))
    print("------------------------------------------")
    option = input(def_translations.translate("Select an option: "))
    if option.lower() == "idioma":
        return "idioma"
    try:
        return int(option)
    except ValueError:
        return -1

# Definicion de la funcion main para ejecutar el programa
def main():
    while True:
        option = menu()
        if isinstance(option, str) and option.lower() == "idioma":
            lang = input("Choose language (en/es): ").strip().lower()
            if lang in ("en", "es"):
                def_translations.set_language(lang)
                print("Language changed!")
            else:
                print("Invalid language.")
            continue
        if option == 1:
            while True:
                try:
                    r = int(input(def_translations.translate("Enter the Reaper's level: ")))
                    p = int(input(def_translations.translate("Enter your character's level: ")))
                    result = formulas.calculate_level(r, p)
                    print("------------------------------------------")
                    print(def_translations.translate("The embryo's level is: {result}").format(result=result))
                    print("------------------------------------------")
                    break  # Exit loop if calculation is successful
                except ValueError as e:
                    print(e)
                    print(def_translations.translate("Please enter valid, non-negative integer values."))
                    print("------------------------------------------")
        elif option == 2:
            lista = choose_list()
            while True:
                try:
                    amount = int(input(def_translations.translate("Amount of tek: ")))
                    item_number = choose_item_or_all(lista)
                    print("------------------------------------------")
                    result = formulas.convertion_tek(amount, lista, item_number if item_number != 0 else None)
                    for item_name, value in result.items():
                        print(f"{def_translations.translate(item_name)}: {value}")
                    print("------------------------------------------")
                    break  # Exit loop if conversion is successful
                except ValueError as e:
                    print(e)
                    print(def_translations.translate("Please enter a valid, non-negative number."))
        elif option == 3:
            create_new_list()
        elif option == 4:
            delete_custom_list()
        elif option == 0:
            print(def_translations.translate("Exiting the program..."))
            break
        else:
            print(def_translations.translate("Invalid option. Please try again."))
            
# Llamada a la funcion main para ejecutar el programa
if __name__ == "__main__":
    main()
# Este es el archivo principal del programa, que importa las funciones del archivo formulas.py