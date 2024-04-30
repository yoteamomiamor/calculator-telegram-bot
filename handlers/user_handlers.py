from email import message
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from lexicon import LEXICON
from keyboards import calculator_keyboard
from callback_data import Callbacks
from . import buttons_handlers


router = Router()
router.include_router(buttons_handlers.router)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON.empty_string,
        reply_markup=calculator_keyboard,
        )


@router.message(Command('help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON.help_message)
