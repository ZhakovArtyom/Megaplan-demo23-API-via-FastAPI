![python](https://img .shields.io/github/languages/top/{username}/{repo-name}?color=yellow)
# Данное приложение реализует взаимодействие с API Megaplan(demo23), с помощью фреймворка FastAPI.
_Основы работы с CRM можно посмотреть в папке src/crm_interaction._

# Инструкция установки
### _*клонирование проекта*_\n
`git clone https://github.com/ZhakovArtyom/Megaplan-demo23-API-via-FastAPI.git`

### _*создание виртуального окружения*_\n
`python3 -m venv venv`

### _*активация виртуального окружения*_\n
`venv\Scripts\activate.bat` - для Windows\n
`source venv/bin/activate` - для Linux и MacOS

### _*установить зависимости*_\n
`pip install -r requirements.txt`\n

### _*заменить файл .env_example на .env и подставить актуальные данные*_

### _*Затем необходимо перейти в корневую папку проекта и запустить команду*_ `uvicorn main:app --reload` для запуска сервера uvicorn*_\n

### _*Далее перейти по ссылке в браузере*_\n
http://127.0.0.1:8000 - для взаимодействия через графический интерфейс\n
http://127.0.0.1:8000/docs - для взаимодействия через Swagger
