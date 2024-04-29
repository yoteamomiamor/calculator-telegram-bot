from email import message
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from lexicon import LEXICON
from keyboards import calculator_keyboard
from callback_data import Callbacks


router = Router()


@router.callback_query(F.data == Callbacks.clear_button_clb)
async def process_clear_button(callback: CallbackQuery):
    if callback.message.text == LEXICON.empty_string:
        pass
    else:
        await callback.message.edit_text(
            text=LEXICON.empty_string,
            reply_markup=calculator_keyboard,
        )

@router.callback_query(F.data == Callbacks.delete_button_clb)
async def process_delete_button(callback: CallbackQuery):
    entry = callback.message.text

    if entry == LEXICON.empty_string:
        pass
    elif len(entry) <= 1:
        await callback.message.edit_text(
            text=LEXICON.empty_string,
            reply_markup=calculator_keyboard,
            )
    else:
        await callback.message.edit_text(
            text=entry[:-1],
            reply_markup=calculator_keyboard,
            )


@router.callback_query(F.data.in_(('0123456789')))
async def process_digit_button(callback: CallbackQuery):
    entry = callback.message.text

    if entry == LEXICON.empty_string:
        await callback.message.edit_text(
            text=callback.data,
            reply_markup=calculator_keyboard,
            )
    else:
        await callback.message.edit_text(
            text=entry + callback.data,
            reply_markup=calculator_keyboard,
            )


@router.callback_query(F.data == LEXICON.min_button_text)
async def process_minus_button(callback: CallbackQuery):
    entry = callback.message.text

    if entry == LEXICON.empty_string:
        await callback.message.edit_text(
            text=callback.data,
            reply_markup=calculator_keyboard,
            )
    else:
        await callback.message.edit_text(
            text=callback.message.text + callback.data,
            reply_markup=calculator_keyboard,
            )


@router.callback_query(F.data == LEXICON.pls_button_text)
async def process_minus_button(callback: CallbackQuery):
    entry = callback.message.text

    if entry == LEXICON.empty_string:
        pass
    elif entry in LEXICON.min_button_text:
        await callback.message.edit_text(
            text=LEXICON.empty_string,
            reply_markup=calculator_keyboard,
            )
    else:
        await callback.message.edit_text(
            text=callback.message.text + callback.data,
            reply_markup=calculator_keyboard,
            )


@router.callback_query(F.data.in_((LEXICON.mul_button_text, LEXICON.div_button_text)))
async def process_minus_button(callback: CallbackQuery):
    entry = callback.message.text

    if entry == LEXICON.empty_string:
        await callback.message.edit_text(
            text=callback.data,
            reply_markup=calculator_keyboard,
            )
    else:
        await callback.message.edit_text(
            text=callback.message.text + callback.data,
            reply_markup=calculator_keyboard,
            )