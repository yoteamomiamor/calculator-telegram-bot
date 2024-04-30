from email import message
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from lexicon import LEXICON
from keyboards import calculator_keyboard
from callback_data import Callbacks
from utils.screen_updaters import *
from utils import calculate


router = Router()
router.callback_query.filter()

_operation_buttons_except_minus = (
    LEXICON.mul_button_text,
    LEXICON.div_button_text,
    LEXICON.pls_button_text,
)


@router.callback_query(F.data == Callbacks.clear_button_clb)
async def process_clear_button(callback: CallbackQuery):
    updated_entry = clear_entry(callback.message.text)

    if updated_entry:
        await callback.message.edit_text(
            text=updated_entry,
            reply_markup=calculator_keyboard,
        )

@router.callback_query(F.data == Callbacks.delete_button_clb)
async def process_delete_button(callback: CallbackQuery):
    updated_entry = delete_last(callback.message.text)

    if updated_entry:
        await callback.message.edit_text(
            text=updated_entry,
            reply_markup=calculator_keyboard,
            )


@router.callback_query(F.data.in_(('0123456789')))
async def process_digit_button(callback: CallbackQuery):
    updated_entry = add_digit(callback.message.text, callback.data)

    await callback.message.edit_text(
        text=updated_entry,
        reply_markup=calculator_keyboard,
        )


@router.callback_query(F.data == Callbacks.point_button_clb)
async def process_point_button(callback: CallbackQuery):
    updated_entry = add_point(callback.message.text)

    if updated_entry:
        await callback.message.edit_text(
            text=updated_entry,
            reply_markup=calculator_keyboard,
            )


@router.callback_query(F.data == LEXICON.min_button_text)
async def process_minus_button(callback: CallbackQuery):
    updated_entry = add_minus(callback.message.text)

    if updated_entry:
        await callback.message.edit_text(
            text=updated_entry,
            reply_markup=calculator_keyboard,
            )


@router.callback_query(F.data.in_(_operation_buttons_except_minus))
async def process_operation_buttons(callback: CallbackQuery):
    updated_entry = add_sign(callback.message.text, callback.data)

    if updated_entry:
        await callback.message.edit_text(
            text=updated_entry,
            reply_markup=calculator_keyboard,
            )


@router.callback_query(F.data == Callbacks.equals_button_clb)
async def process_equals_button(callback: CallbackQuery):
    await callback.message.edit_text(
            text=calculate(callback.message.text),
            reply_markup=calculator_keyboard,
            )
