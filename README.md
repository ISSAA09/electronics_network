# Онлайн платформа торговой сети электроники

---
### Описание:

Данная работа представляет собой **backend-часть** для веб-приложения, с API интерфейсом и админ-панелью.
<p>


------------------------------------------------------------------------------------------------

### Функционал:
- Разработана модель иерархической структуры сети по продаже электроники, состоящей из трех уровней: завод, розничная сеть, индивидуальный предприниматель
- Каждое звено сети содержит данные о названии, контактах, продуктах, поставщике, задолженности и времени создания
- В админ-панели доступен вывод созданных объектов
- На странице объекта сети добавлена ссылка на "Поставщика", фильтр по названию города и "admin action" для очистки задолженности перед поставщиком
- Используя Django REST framework (DRF), создан набор представлений для CRUD операций с моделью поставщика, с фильтрацией по стране
- Настроены права доступа к API, позволяющие доступ только активным сотрудникам.

----------------------------------------------------------------
### Стэк

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/Framework-DRF-informational?style=flat&logo=Django&logoColor=white&color=green)
![](https://img.shields.io/badge/database-Postgresql-informational?style=flat&logo=postgresql&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=green)

### Технологии:
- Python
- Django
- Django REST framework
- psycopg2-binary
- JWT 
- DRF-YASG
- CORS
- Docker
- Docker Compose

------------------------------------------------------------------------------------------------

### Запуск проекта 
<h4>Локально:</h4>

1. Установить локально на свой компьютер Python версией не ниже 3.10.x!
2. Клонировать файлы проекта с GitHub репозитория:
- > https://github.com/ISSAA09/electronics_network.git
3. Создать виртуальное окружение:
- `python -m venv venv`
4. Активировать виртуальное окружение:
- `venv/Scripts/activate (Windows)`
- `source venv/bin/activate (Linux, MacOS)`
5. Установить зависимости:
- `pip install -r requirements.txt`
6. Создать файл .env c переменными окружения.
7. Добавить в файл настройки, как в .env.sample и заполнить их.
8. Создайте базу данных, выполните `python manage.py migrate`. 
9. Создайте администратора, выполните `python manage.py csu`. 
10. Запустите сервер разработки, выполните `python manage.py runserver`. 
11. Перейдите в веб-браузере по адресу http://localhost:8000 и вы увидите главную страницу сервиса.

<h4>Запуск проекта через docker-compose:</h4>

1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.sample
4. Соберите образ с помощью команды `docker-compose build`
5. Запустите контейнеры с помощью команды `docker-compose up`
> Сборка и запуск контейнера в фоновом режиме:
> docker-compose up -d --build

----------------------------------------------------------------

### Авторы

ISSAA09

----------------------------------------------------------------
### Связь с авторами

https://github.com/ISSAA09

