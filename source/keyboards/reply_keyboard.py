from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


button_test_mode = KeyboardButton(text="🧪 На тестовых данных")
button_prod_mode = KeyboardButton(text="🛠 На реальных данных")

keyboard = ReplyKeyboardMarkup(keyboard=[[button_test_mode, button_prod_mode]],
                               resize_keyboard=True, one_time_keyboard=True)
