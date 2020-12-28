# Интерактивная карта Where to go
# Что умеет
Красиво отображает точки на карте с описаниями и картинками.
Деплой сайта: 
[https://artemvolik.pythonanywhere.com/](https://artemvolik.pythonanywhere.com/)  
![screenshot](/main.png?raw=true)  


## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Запустите разработческий сервер

```
python3 manage.py runserver
```
## Попасть в админку:

Создать суперпользователя админки 
```sh
python3 manage.py createsuperuser
```
Войти с этими данными `<адрес_сайта>/admin`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `DB_NAME` — путь до базы данных, например: `schoolbase.sqlite3`

## Использование
Модели просты, действия в админке интуитивно понятны.

## Загрузить точки 
Выполнив 
```shell
python3 manage.py load_place http://адрес/файла.json
```
вы можете автоматичесски загрузить данные в базу. Скрипт ожидает данные в [таком формате](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9B%D0%BE%D0%BF%D0%B0%D1%82%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA.json).


