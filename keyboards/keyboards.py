from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON_RU


builder = InlineKeyboardBuilder()


calculator_keyboard = builder.row(
    InlineKeyboardButton(text='1'),
    width=4,
)
