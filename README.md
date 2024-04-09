# Megaplan API Demo via FastAPI

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI Version](https://img.shields.io/badge/FastAPI-0.110.1-green.svg)
![aiohttp Version](https://img.shields.io/badge/aiohttp-3.9.3-blue.svg)

Данное приложение реализует взаимодействие с API Megaplan (demo23) с помощью фреймворка FastAPI. Основы работы с CRM можно изучить в папке `src/crm_interaction`.

## Инструкция установки

### Клонирование проекта
```bash
git clone https://github.com/ZhakovArtyom/Megaplan-demo23-API-via-FastAPI.git
```
### Создание виртуального окружения
```bash
python3 -m venv venv
```
### Активация виртуального окружения
* Для Windows:
```bash
venv\Scripts\activate.bat
```
* Для Linux и MacOS:
 ```bash
source venv/bin/activate
```
### Установка зависимостей
```bash
pip install -r requirements.txt
```
### Заменить файл .env_example на .env и подставить актуальные данные
### Запуск сервера
Перейдите в корневую папку проекта и запустите команду:
 ```bash
uvicorn main:app --reload
```
Это запустит сервер uvicorn с автоматической перезагрузкой.
### Взаимодействие через браузер
* Для графического интерфейса перейдите по ссылке: http://127.0.0.1:8000
* Для взаимодействия через Swagger UI перейдите по ссылке: http://127.0.0.1:8000/docs

