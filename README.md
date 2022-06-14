# Установка
Работоспособность проверена на Ubuntu 22.04 и Python 3.7.

На чистой системе без пакета `wheel` установка остальных не выполняется корректно.
```
pip install wheel
```
Установка зависимостей:
```
pip install -r requirements.txt
```
Выполнение миграций БД:
```
python manage.py migrate
```

# Запуск
```
python manage.py runserver
```
