# ![](https://github.com/yasumichi/DriedPotato/blob/main/items/static/items/images/DriedPotato.png)DriedPotato

DriedPotato manage what your team wants.

## Environment

- Python 3.10+
- Django 5.0.x
- django-mathfilters
- asgiref
- sqlparse

## Initial setup

### Install requirement packages

```
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```

### Setup database

Edit `DATABASES` in [DriedPotato/settings.py](DriedPotato/settings.py).

See [Databases | Django documentation | Django](https://docs.djangoproject.com/en/5.0/ref/databases/).

### Create database tables


```
$ python manage.py migrate
```

### Create super user

```
$ python manage.py createsuperuser
```

## Run development server


```
$ python manage.py runserver
```

- Application: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin site: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Deployment

See [How to deploy Django | Django documentation | Django](https://docs.djangoproject.com/en/5.0/howto/deployment/).
