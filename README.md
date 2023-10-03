Тестовое задание

Разработка онлайн платформы торговой сети электроники.


Установить зависимости pip install -r requirements.txt

Создать .env файл, в нем прописать все свои данные, что есть в .env.example

Создайте базу данных psql -U (ваш логин в постгрес).

Зайти в config/settings.py и загнать в DATABASES: HOST, PORT под #

Произвести миграцию таблиц в базу данных python manage.py migrate

Запустить сервер python manage.py runserver
