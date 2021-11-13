# Бюджет

* Python
* Django
* SQLite3
* Docker/Docker-compose

## Licence

MIT

### Запустить проект
> docker-compose up

### Миграции
> docker-compose run web python manage.py makemigrations

> docker-compose run web python manage.py migrate

### Создать супер пользователя
> docker-compose run web python manage.py createsuperuser

### Загрузка фикстур (внутри докера)
> python manage.py loaddata 001_categories