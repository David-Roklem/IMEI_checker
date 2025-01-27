# Inroduction
Данный проект представляет собой Telegram-бот, реализующий функционал проверки IMEI цифровых устройств через сервис [https://imeicheck.net/](https://imeicheck.net/)

## Getting Started
Склонировать данный репозиторий одним из способов (HTTPS или SSH):
```
git clone https://github.com/David-Roklem/IMEI_checker.git
git clone git@github.com:David-Roklem/IMEI_checker.git
```

### Dependencies
Все требуемые зависимости перечислены в файлах pyproject.toml и requirements.txt.

### Installing
В случае использования pip, зависимости можно установить командой:
```
pip install -r requirements.txt
```
При использовании пакетных менеджеров uv или poetry, вот ссылки на их документации [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/), [https://python-poetry.org/](https://python-poetry.org/)

### Executing program
1) Прежде всего, необходимо сконфигурировать файл .env по примеру файла .env.example
2) Для контроля доступа прописать в переменную `USERS_WHITELIST` по пути `source/config_data/config.py` TG id пользователей, которым будет открыт доступ к боту
2) Запустить файл source/main.py из корневой директории проекта командой `python source/main.py`

### Project improvement
*Список возможных (необходимых) улучшений:*

🔭Реализовать белый список пользователей через БД (Mongo или Redis, например)

🔭Текущая реализация FSM не сохранит данные о состояниях в случае сбоя (вместо стандартного MemoryStorage применить Redis)

🔭Сборка проекта в докер-образ в случае интеграции БД

🔭Обработка нерелевантных сообщений вне команд и логики бота
