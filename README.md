# Сервис по размещению объявлений

**Проект "posting_ads" - это сайт, на котором пользователи могут публиковать объявления. Основные роли системы - пользователь и администратор. Пользователь может зарегистрироваться на сайте и впоследствии входить в систему. Авторизация выполнена с помощью JWT-токена.**

**Возможности пользователя:**
* Писать статьи
* Редактировать и удалять только свои статьи
* Просматривать список всех статей
* Детально просматривать каждую статью
* Писать комментарии к статьям
* Редактировать и удалять только свои комментарии к статьям

**Возможности администратора:**
* Всё выше перечисленное
* Удалять любые статьи и комментарии к ним
* Назначать пользователя администратором
* Блокировать пользователей

**Дополнительный функционал проекта:**
* Пагинация
* Фильтрация объйявлений (по дате публикации)
* Поиск объявлений (по словам из заголовка)
* Сортировка выдачи объявлений (по автору и дате публикации)

**Инструменты и стек:**
* Python
* Django
* Django REST Framework
* API
* Postman
* JWT

**Как запустить проект:**
* Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AnnaPrilutskaya/posting_ads.git
```

```
cd posting_ads
```

* Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate 
```

* Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

* Выполнить миграции:

```
python manage.py migrate
```

* Запустить проект:

```
python manage.py runserver
```