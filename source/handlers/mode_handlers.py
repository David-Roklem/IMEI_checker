from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from FSM.states import UserInputStates
from helpers.helper_functions import check_imei_input, get_service_id
from texts.bot_texts import TEXTS_ANSWERS
from keyboards.inline_keyboard import create_inline_kb

mode_router = Router()


@mode_router.message(F.text == '🧪 На тестовых данных')
async def handle_test_button(message: Message, state: FSMContext):
    """Обработка кнопки '🧪 На тестовых данных'"""
    await message.answer(TEXTS_ANSWERS["test_mode_chosen"])
    await message.answer(TEXTS_ANSWERS["ask_for_imei"], reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserInputStates.test_mode)


@mode_router.message(StateFilter(UserInputStates.test_mode))
async def handle_test_mode(message: Message, state: FSMContext):
    """Обработка сообщения с полученным IMEI устройства для тестовых данных"""
    msg_text = message.text
    res = await check_imei_input(msg_text, state, test_data=True)
    await message.answer(res)


@mode_router.message(StateFilter(UserInputStates.prod_mode))
async def handle_prod_mode(message: Message, state: FSMContext):
    """Обработка сообщения с полученным IMEI устройства для реальных данных"""
    msg_text = message.text
    state_data = await state.get_data()
    service_id = state_data.get("service_id")
    res = await check_imei_input(msg_text, state, prod_data=True, service_id=service_id)
    await message.answer(res)


@mode_router.message(F.text == '🛠 На реальных данных')
async def handle_real_button(message: Message):
    """Обработка кнопки '🛠 На реальных данных'"""
    await message.answer(TEXTS_ANSWERS["real_data_mode_chosen_1"], reply_markup=ReplyKeyboardRemove())
    inline_keyboard = create_inline_kb()
    await message.answer(TEXTS_ANSWERS["real_data_mode_chosen_2"], reply_markup=inline_keyboard)


@mode_router.callback_query(F.data.startswith('service_'))
async def process_service_callback(callback: CallbackQuery, state: FSMContext):
    """Обработка callback-события при нажатии на инлайн-клавиатуру"""
    service_id = int(get_service_id(callback))
    await callback.message.edit_text(text=TEXTS_ANSWERS["ask_for_imei"])
    await state.set_state(UserInputStates.prod_mode)
    await state.set_data({"service_id": service_id})
