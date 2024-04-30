from lexicon import LEXICON


def is_digit(symbol: str) -> bool:
    return symbol.isdigit()


def is_sign(symbol: str) -> bool:
    return symbol in (
        LEXICON.min_button_text,
        LEXICON.pls_button_text,
        LEXICON.div_button_text,
        LEXICON.mul_button_text,
    )
