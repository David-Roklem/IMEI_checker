from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from checker.api import IMEIChecker
from texts.bot_texts import TEXTS_ANSWERS
from config_data.service_ids import services_data


async def check_imei_input(msg_text: str, state: FSMContext, test_data: bool = False, prod_data: bool = False,
                           service_id: int = None):
    """Обрабатывает IMEI отправленный юзером, валидируя его и отправляя запрос к чекеру IMEI

    :param msg_text: текст, полученный от юзера, содержащий IMEI.
    :param test_data: если True, то запрос в режиме тестовых данных.
    :param prod_data: если True, то запрос в режиме реальных данных.
    :param service_id: id сервиса в системе IMEI чекера.
    :return: Сообщение с данными о IMEI, полученными от чекера либо информацию о том, что не удалось их получить"""
    if msg_text.isdigit() and 8 <= len(msg_text) <= 15:
        if test_data:
            res = await IMEIChecker().test_check_imei(msg_text)
        elif prod_data:
            res = await IMEIChecker().check_imei(msg_text, service_id)
        await state.clear()
        return res.text
    else:
        return TEXTS_ANSWERS["invalid_imei"]


def get_service_id(callback_query: CallbackQuery):
    service_id = int(callback_query.data.split('_')[1])
    return service_id
