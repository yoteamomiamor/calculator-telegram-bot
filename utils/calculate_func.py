from lexicon import LEXICON

def calculate(entry: str) -> str:
    try:
        return entry + LEXICON.equals_button_text + eval(entry)
    except:
        return LEXICON.error
