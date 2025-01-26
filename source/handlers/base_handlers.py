from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from texts.bot_texts import TEXTS_CMD
from keyboards.reply_keyboard import keyboard

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """Обработка команды '/start'"""
    await message.answer(TEXTS_CMD[message.text], reply_markup=keyboard)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    """Обработка команды '/help'"""
    await message.answer(TEXTS_CMD[message.text], reply_markup=ReplyKeyboardRemove())
