from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from texts.bot_texts import TEXTS_CMD
from keyboards.reply_keyboard import keyboard

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    """Обработка команды '/start'"""
    await message.answer(TEXTS_CMD[message.text], reply_markup=keyboard)
    await state.clear()


@router.message(Command(commands='help'))
async def process_help_command(message: Message, state: FSMContext):
    """Обработка команды '/help'"""
    await message.answer(TEXTS_CMD[message.text], reply_markup=ReplyKeyboardRemove())
    await state.clear()
