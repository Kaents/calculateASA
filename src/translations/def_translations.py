import json
import os

TRANSLATIONS_PATH = os.path.join(os.path.dirname(__file__), "translations.json")
LANG_PATH = os.path.join(os.path.dirname(__file__), "lang.json")

# Loads all translations from the JSON file
def load_translations():
    with open(TRANSLATIONS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Gets the current language from the lang.json file, defaults to 'en' if not set
def get_current_language():
    if not os.path.exists(LANG_PATH):
        set_language("en")
    with open(LANG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("lang", "en")

# Sets the current language and saves it to lang.json
def set_language(lang_code):
    with open(LANG_PATH, "w", encoding="utf-8") as f:
        json.dump({"lang": lang_code}, f)

# Translates the given text according to the current language
def translate(text, **kwargs):
    lang = get_current_language()
    translations = load_translations()
    # Search for the translation in the current language, if it does not exist, use the original text.
    if lang in translations:
        translated = translations[lang].get(text, text)
        if kwargs:
            return translated.format(**kwargs)
        return translated
    else:
        if kwargs:
            return text.format(**kwargs)
        return text