# AbeloHost Test Task

## 📦 Установка

### 1. Склонируйте репозиторий и перейдите в корневую директорию проекта
```
$> git clone git@github.com:Flawlesse/TestWork13.git
$> cd TestWork13
```
### 2. Внутри корневой директории создайте файл с названием `.env`
```
$> touch .env
```
Запишите в него недостающие пароли (на ваш выбор, главное чтобы они не были пустыми). Можно использовать спец. символы, английский алфавит и цифры.
В качестве шаблона используйте файл `example.env` из корневой директории. Это набор ENV переменных, которые необходимо использовать. Не забудьте сохранить файл `.env` :)
#### Вот пример того как должен выглядеть итоговый `.env`:
```
$> cat .env

MONGO_HOST=mongodb
MONGO_DBNAME=quotedb
MONGO_INITDB_ROOT_USERNAME=mdbroot
MONGO_INITDB_ROOT_PASSWORD=n!nN3U89e!AXx00}3-MXsnn**}\

ME_CONFIG_BASICAUTH_USERNAME=admin
ME_CONFIG_BASICAUTH_PASSWORD=x.nn!n4:aie7asd--+xx3!!

REDIS_HOST=redis

$>
```
### 3. Запустите проект
```
$> docker compose up --build
```
### 4. По завершении проверки работы, выполните эту команду
```
$> docker compose down
```
### !!! ВАЖНО:
- Основные пути начинаются с http://localhost/api/ (e.g. GET http://localhost/api/quotes)
- Для доступа к Swagger UI перейдите сюда http://localhost/docs/
- Вы также можете воспользоваться WebUI для MongoDB (MongoExpress) вот здесь http://localhost:8081 и посмотреть наличие данных в коллекции `quotes`
