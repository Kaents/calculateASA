# Formulas for conversion and creature level calculation
import translations.def_translations as def_translations
"""
    Embryo level calculation in the game Reapers
    r = Reaper's level
    p = Your character's level
    e = Embryo's level without adding the 75 base points.
    final_level = Final level of the embryo after adding the 75 base points.
"""
def calculate_level(r, p):
    if r < 0 or p < 0:
        raise ValueError(def_translations.translate("Levels cannot be negative."))
    e = r * (p + 100) / 250
    return int(e + 75)

"""
    Function for the equivalence list of 100 tek.
    quantity_tek = Amount of tek to convert.
    convertion = Dictionary of the equivalence for 100 tek.
    In the iteration, the amount of tek is multiplied by the equivalence value and rounded.
"""
def convertion_tek(quantity_tek, convertion_dict, item_number=None):
    if quantity_tek < 0:
        raise ValueError(def_translations.translate("The amount of tek cannot be negative."))
    result = {}
    if item_number is not None:
        item = convertion_dict.get(str(item_number))
        if not item:
            raise ValueError("Invalid item number.")
        result[item["name"]] = round((quantity_tek / 100) * item["value"])
    else:
        for item in convertion_dict.values():
            result[item["name"]] = round((quantity_tek / 100) * item["value"])
    return result
