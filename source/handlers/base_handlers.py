from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from texts.bot_texts import TEXTS_CMD

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """Обработка команды '/start'"""
    await message.answer(TEXTS_CMD[message.text])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    """Обработка команды '/help'"""
    await message.answer(TEXTS_CMD[message.text])
