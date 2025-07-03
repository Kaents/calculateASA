import convertions.tek_convertions as tek_convertions
import translations.def_translations as def_translations

# Functions to create, choose, and delete custom conversion lists
def create_new_list():
    default_convertion = tek_convertions.get_default_convertion()
    new_list = {}
    print(def_translations.translate("Create a new custom conversion list."))
    print(def_translations.translate("To skip an item, just press Enter without typing anything."))
    for num, item in default_convertion.items():
        entry = input(def_translations.translate("Value for '{item}': ").format(item=f"{num}. {def_translations.translate(item['name'])}"))
        if entry.strip() == "":
            continue
        try:
            value = int(entry)
            new_list[num] = {"name": item["name"], "value": value}
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
        #Agregar traduccion para "y" al agregar idioma
        if confirm.lower() == "y" or confirm.lower() == "s":
            tek_convertions.remove_custom_convertion(selection - 1)
            print(def_translations.translate("List '{name}' deleted.").format(name=name))
        else:
            print(def_translations.translate("Operation cancelled."))
    else:
        print(def_translations.translate("Operation cancelled."))

# Function to choose an item or all items for conversion lists
def choose_item_or_all(convertion_dict):
    print("------------------------------------------")
    print(def_translations.translate("Choose an item to convert or 0 for all:"))
    for num, item in convertion_dict.items():
        print(f"{num}. {def_translations.translate(item['name'])}")
    print("0. " + def_translations.translate("All items"))
    while True:
        try:
            selection = int(input(def_translations.translate("Enter the item number: ")))
            if selection == 0 or str(selection) in convertion_dict:
                return selection
            else:
                print(def_translations.translate("Invalid selection. Try again."))
        except ValueError:
            print(def_translations.translate("Please enter a valid number."))