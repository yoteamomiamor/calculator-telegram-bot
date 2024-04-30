from lexicon import LEXICON

def calculate(entry: str) -> str | bool:
    try:
        return ' '.join((
            entry,
            LEXICON.equals_button_text,
            str(eval(entry))
        ))
    except:
        return False
