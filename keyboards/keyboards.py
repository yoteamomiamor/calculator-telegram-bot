from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON_RU
from callback_data import Callbacks


ikb_builder = InlineKeyboardBuilder()


clear_button = InlineKeyboardButton(
    text=LEXICON_RU.clear_button_text,
    callback_data=Callbacks.clear_button_clb,
    )

delete_button = InlineKeyboardButton(
    text=LEXICON_RU.delete_button_text,
    callback_data=Callbacks.delete_button_clb,
    )

point_button = InlineKeyboardButton(
    text=LEXICON_RU.point_button_text,
    callback_data=Callbacks.point_button_clb,
    )

equals_button = InlineKeyboardButton(
    text=LEXICON_RU.equals_button_text,
    callback_data=Callbacks.equals_button_clb,
    )

ikb_builder.row(
    clear_button,
    delete_button,
    point_button,
    InlineKeyboardButton(text=LEXICON_RU.pls_button_text, callback_data=LEXICON_RU.pls_button_text),
    *[
        InlineKeyboardButton(
            text=str(i),
            callback_data=str(i),
            )
        for i in range(7, 10)
        ],
    InlineKeyboardButton(text=LEXICON_RU.div_button_text, callback_data=LEXICON_RU.div_button_text),
    *[
        InlineKeyboardButton(
            text=str(i),
            callback_data=str(i),
            )
        for i in range(4, 7)
        ],
    InlineKeyboardButton(text=LEXICON_RU.mul_button_text, callback_data=LEXICON_RU.mul_button_text),
    *[
        InlineKeyboardButton(
            text=str(i),
            callback_data=str(i),
            )
        for i in range(1, 4)
        ],
    InlineKeyboardButton(text=LEXICON_RU.min_button_text, callback_data=LEXICON_RU.min_button_text),
    InlineKeyboardButton(text='0', callback_data='0'),
    equals_button,

    width=4,
)

calculator_keyboard = ikb_builder.as_markup()
