import json
import os

TRANSLATIONS_PATH = os.path.join(os.path.dirname(__file__), "translations.json")
LANG_PATH = os.path.join(os.path.dirname(__file__), "lang.json")

def load_translations():
    with open(TRANSLATIONS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def get_current_language():
    if not os.path.exists(LANG_PATH):
        set_language("en")
    with open(LANG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("lang", "en")

def set_language(lang_code):
    with open(LANG_PATH, "w", encoding="utf-8") as f:
        json.dump({"lang": lang_code}, f)

def translate(text, **kwargs):
    lang = get_current_language()
    if lang == "es":
        translations = load_translations()
        translated = translations.get(text, text)
        if kwargs:
            return translated.format(**kwargs)
        return translated
    else:
        if kwargs:
            return text.format(**kwargs)
        return text