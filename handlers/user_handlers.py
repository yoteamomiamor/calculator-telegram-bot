from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from lexicon import LEXICON_RU
from keyboards import calculator_keyboard


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU.start_message,
        reply_markup=calculator_keyboard,
        )


@router.message(Command('help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU.help_message)
