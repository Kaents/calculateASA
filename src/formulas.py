#formulas para calculo de conversion y nivel de criatura
"""
    Calculo de niveles de embriones en el juego de Reapers
    r = Nivel de la Reaper
    p = Nivel de tu personaje
    e = Nivel del embrion sin sumar los 75 puntos base.
    final_level = Nivel final del embrion despues de la suma de los 75 puntos base.
"""
def calculate_level(r, p):
    if r < 0 or p < 0:
        raise ValueError("Los niveles no pueden ser negativos.")
    e = r * (p + 100) / 250
    return int(e + 75) 

"""
    Función de la lista de equivalencias de 100 tek.
    quantity_tek = Cantidad de tek a convertir.
    convertion = Diccionario de la equivalencia de 100 tek.
    en la interacion se multiplica la cantidad de tek por el valor de la equivalencia (value) y se redondea.
"""
import convertions.tek_convertions as tek_convertions

def convertion_tek(quantity_tek, convertion_dict=None):
    if quantity_tek < 0:
        raise ValueError("La cantidad de tek no puede ser negativa.")
    if convertion_dict is None:
        convertion_dict = tek_convertions.default_convertion
    result = {}
    for item, value in convertion_dict.items():
        result[item] = round((quantity_tek / 100) * value)
    return result
