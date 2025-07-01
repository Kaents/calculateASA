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
import convertions.tek_convertions as tek_convertions

def convertion_tek(quantity_tek, convertion_dict=None):
    if quantity_tek < 0:
        raise ValueError(def_translations.translate("The amount of tek cannot be negative."))
    if convertion_dict is None:
        convertion_dict = tek_convertions.default_convertion
    result = {}
    for item, value in convertion_dict.items():
        result[item] = round((quantity_tek / 100) * value)
    return result
