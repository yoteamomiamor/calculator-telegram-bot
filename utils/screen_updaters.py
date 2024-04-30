from utils import is_sign
from lexicon import LEXICON


def add_digit(entry: str, digit: str) -> str:
    space = ' ' if is_sign(entry[-1]) else ''

    if entry == LEXICON.empty_string:
        return digit
    else:
        return entry + space + digit


def add_point(entry: str) -> str | bool:
    splitted = entry.split()

    if LEXICON.point_button_text in splitted[-1] or is_sign(splitted[-1]):
        return False
    elif splitted[-1].isdigit():
        return entry + LEXICON.point_button_text
    else:
        return False


def add_minus(entry: str) -> str | bool:

    if entry[-1] == LEXICON.min_button_text:
        return False
    elif entry == LEXICON.empty_string or is_sign(entry[-1]):
        return entry[:-1] + LEXICON.min_button_text
    else:
        return entry + ' ' + LEXICON.min_button_text


def add_sign(entry: str, sign: str) -> str | bool:
    updated_entry = entry

    if entry == LEXICON.min_button_text:
        updated_entry = LEXICON.empty_string
    elif entry == LEXICON.empty_string:
        return False
    elif is_sign(entry[-1]):
        updated_entry = entry[:-1] + sign
    elif entry[-1] == LEXICON.point_button_text:
        updated_entry = entry[:-1] + ' ' + sign
    else:
        updated_entry = entry + ' ' + sign

    if updated_entry == entry:
        return False
    return updated_entry


def clear_entry(entry: str) -> str | bool:
    if entry == LEXICON.empty_string:
        return False
    else:
        return LEXICON.empty_string


def delete_last(entry: str) -> str | bool:
    if entry == LEXICON.empty_string:
        return False
    elif len(entry) <= 1:
        return LEXICON.empty_string
    else:
        return entry[:-1]
