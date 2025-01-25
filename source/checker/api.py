import httpx
from config_data.config import config, IMEI_CHECKER_BASE_URL, CUSTOM_REQ_TIMEOUT


class IMEIChecker:

    def __init__(self) -> None:
        self.base_url = IMEI_CHECKER_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {config.token_api_sandbox}",
            "Accept-Language": "en",
        }
        self.headers_sandbox = {
            "Authorization": f"Bearer {config.token_api_sandbox}",
            "Accept-Language": "en",
        }

    async def check_imei(self, device_imei: str, service_id: int):
        """Отправляет запрос на проверку IMEI устройства"""
        url = self.base_url + "v1/checks"
        payload = {
            "deviceId": device_imei,
            "serviceId": service_id,
            }
        async with httpx.AsyncClient(timeout=CUSTOM_REQ_TIMEOUT) as client:
            res = await client.post(url=url, headers=self.headers, json=payload)
        return res.json()

    async def test_check_imei(self, device_imei: str):
        """Отправляет тестовый запрос на получение моковых данных.

        Проверить валидные service_id можно по эндпоинту /v1/services"""
        url = self.base_url + "v1/checks"
        payload = {
            "deviceId": device_imei,
            "serviceId": 12,  # захардкожен serviceId для успешных моковых ответов
            }
        async with httpx.AsyncClient(timeout=CUSTOM_REQ_TIMEOUT) as client:
            res = await client.post(url=url, headers=self.headers_sandbox, json=payload)
        return res
