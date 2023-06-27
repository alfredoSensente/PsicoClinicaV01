# Psycoclinic

This is a clinic system.

## Python Version

The project needs python 3.11.3

## Requierements

Install all dependencies in requirements.txt
```shell
$ pip install -r requirements.txt
```

## Docker Implementation

1. Run docker and build the containers(You must have a .env file):
```shell
$ docker-compose build
```

2. Up the docker containers with the next command:
```shell
$ docker-compose up -d
```

3. In a container shell, type the next command to create a superuser(you must do this step only once):
```shell
$ python manage.py shell
```
```python
>>> from users.models import CustomUser
>>> CustomUser.objects.create_superuser(email='admin@mail.com',password='admin',is_staff=True,is_superuser=True)
>>> exit()
```

4. Down the containers:
```shell
$ docker-compose down
```
