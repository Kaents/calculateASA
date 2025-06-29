#main de la aplicacion para el calculo de conversion y nivel de criatura
import formulas
import convertions.tek_convertions as tek_convertions
import translations.def_translations as def_translations

# Definicion de la funcion menu para que el usuario seleccione la opcion deseada 
def menu():
    print(def_translations.translate("\nWelcome to the conversion and creature level calculator"))
    print(def_translations.translate("1. Embryo level calculation"))
    print(def_translations.translate("2. Tek conversion calculation"))
    print(def_translations.translate("3. Create new conversion list"))
    print(def_translations.translate("4. Delete custom conversion list"))
    print(def_translations.translate("0. Exit"))
    print(def_translations.translate("------------------------------------------"))
    option = input(def_translations.translate("Select an option: "))
    if option.lower() == "idioma":
        return "idioma"
    try:
        return int(option)
    except ValueError:
        return -1

def create_new_list():
    default_convertion = tek_convertions.get_default_convertion()
    new_list = {}
    print(def_translations.translate("Create a new custom conversion list."))
    print(def_translations.translate("To skip an item, just press Enter without typing anything."))
    for item in default_convertion:
        entry = input(def_translations.translate("Value for '{item}' (leave empty to skip): ").format(item=item))
        if entry.strip() == "":
            continue
        try:
            value = int(entry)
            new_list[item] = value
        except ValueError:
            print(def_translations.translate("Invalid value, this item will be skipped."))
    name = input(def_translations.translate("Give a name to your custom list: ")).strip()
    if not name:
        name = f"Custom {len(tek_convertions.get_custom_convertions())+1}"
    tek_convertions.add_custom_convertion(name, new_list)
    print(def_translations.translate("List '{name}' saved!").format(name=name))

def choose_list():
    default_convertion = tek_convertions.get_default_convertion()
    custom_convertions = tek_convertions.get_custom_convertions()
    print(def_translations.translate("Choose the conversion list:"))
    print(def_translations.translate("0. Default"))
    for idx, lista in enumerate(custom_convertions, 1):
        print(f"{idx}. {lista['name']}")
    selection = int(input(def_translations.translate("Select the list number: ")))
    if selection == 0:
        return default_convertion
    elif 1 <= selection <= len(custom_convertions):
        return custom_convertions[selection - 1]["items"]
    else:
        print(def_translations.translate("Invalid selection, using default."))
        return default_convertion

def delete_custom_list():
    custom_convertions = tek_convertions.get_custom_convertions()
    if not custom_convertions:
        print(def_translations.translate("There are no custom lists to delete."))
        return
    print(def_translations.translate("Custom lists:"))
    for idx, lista in enumerate(custom_convertions, 1):
        print(f"{idx}. {lista['name']}")
    selection = int(input(def_translations.translate("Select the number of the list to delete (0 to cancel): ")))
    if 1 <= selection <= len(custom_convertions):
        name = custom_convertions[selection - 1]["name"]
        confirm = input(def_translations.translate("Are you sure you want to delete '{name}'? (y/n): ").format(name=name))
        if confirm.lower() == "y" or "s":
            tek_convertions.remove_custom_convertion(selection - 1)
            print(def_translations.translate("List '{name}' deleted.").format(name=name))
        else:
            print(def_translations.translate("Operation cancelled."))
    else:
        print(def_translations.translate("Operation cancelled."))

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
            r = int(input(def_translations.translate("Enter the Reaper's level: ")))
            p = int(input(def_translations.translate("Enter your character's level: ")))
            try:
                result = formulas.calculate_level(r, p)
                print(def_translations.translate("------------------------------------------"))
                print(def_translations.translate("The embryo's level is: {result}").format(result=result))
                print(def_translations.translate("------------------------------------------"))
            except ValueError as e:
                print(e)
        elif option == 2:
            lista = choose_list()
            amount = int(input(def_translations.translate("Amount of tek: ")))
            print(def_translations.translate("------------------------------------------"))
            print(formulas.convertion_tek(amount, lista))
            print(def_translations.translate("------------------------------------------"))
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