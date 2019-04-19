# task-8

## Описание
Вебсервер, предоставляющий API для изменения размера картинок.
Необходим локальный запуск rq worker.
Необходим локальный запуск redis (on Windows).


### Запуск rq worker
* `rq worker high`

### Запуск сервера
* `set FLASK_APP=api.wsgi` on Windows
* `export FLASK_APP=api.wsgi` on Linux and Mac
* `flask run`

### Запуск тестов
* `python -m pytest`

### Запуск линтера
* `flake8 api/`
