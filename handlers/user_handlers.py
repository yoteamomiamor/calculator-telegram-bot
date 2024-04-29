from email import message
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from lexicon import LEXICON
from keyboards import calculator_keyboard
from callback_data import Callbacks


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON.start_message,
        reply_markup=calculator_keyboard,
        )


@router.message(Command('help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON.help_message)


@router.callback_query(F.data == Callbacks.clear_button_clb)
async def process_clear_button(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON.empty_string,
        reply_markup=calculator_keyboard,
    )

@router.callback_query(F.data == Callbacks.delete_button_clb)
async def process_delete_button(callback: CallbackQuery):
    entry = callback.message.text
    print(entry)

    if len(entry) <= 1:
        await callback.message.edit_text(
        text=LEXICON.empty_string,
        reply_markup=calculator_keyboard,
    )
    else:
        await callback.message.edit_text(
        text=LEXICON.empty_string[:-1],
        reply_markup=calculator_keyboard,
    )
