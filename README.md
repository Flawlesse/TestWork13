# AbeloHost Test Task

## 📦 Установка

### 1. Склонируйте репозиторий и перейдите в корневую директорию проекта
```
$> git clone git@github.com:Flawlesse/TestWork13.git
$> cd TestWork13
```
### 2. Запустите проект
```
$> docker compose up --build
```
### 3. По завершении проверки работы, выполните эту команду
```
$> docker compose down
```
### ВАЖНО:
- Основные пути начинаются с http://localhost/api/ (e.g. GET http://localhost/api/quotes)
- Для доступа к Swagger UI перейдите сюда http://localhost/docs/
- Вы также можете воспользоваться WebUI для MongoDB (MongoExpress) вот здесь http://localhost:8081 и посмотреть наличие данных в коллекции `quotes`