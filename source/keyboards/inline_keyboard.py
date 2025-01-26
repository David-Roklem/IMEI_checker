from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config_data.service_ids import services_data


def create_inline_kb(width: int = 2) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for service in services_data:
        button = InlineKeyboardButton(
            text=f"{service['title']} - ${service['price']}",
            callback_data=f"service_{service['id']}"
        )
        buttons.append(button)
    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()
