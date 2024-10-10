# ProdManager

## Описание проекта

ProdManager — это веб-приложение для управления списком продуктов. Оно предоставляет REST API для выполнения операций создания, обновления, удаления и поиска продуктов. Каждый продукт может иметь одно изображение. 

### Основные возможности:
- Создание продуктов
- Обновление продуктов
- Удаление продуктов
- Поиск продуктов с использованием полнотекстового поиска
- Фильтрация продуктов по категориям
- Авторизация пользователей


## Установка и запуск

### Необходимые зависимости

- Docker
- Docker Compose

### Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/sntx10/ProdManager.git
   cd ProdManager
   ```

2. Скопируйте файл .env.example в .env и настройте переменные окружения по вашему усмотрению:
   ```bash
    cp .env.example .env
   ```
3. Запустите контейнеры:
   ```bash
   make up
   ```
4. После запуска проекта, API будет доступен по адресу http://localhost:8000.

## Примеры запросов

## Примеры запросов для пользователей
1. Регистрация пользователя
   Для регистрации нового пользователя отправьте POST-запрос на следующий URL:

```bash

POST http://localhost:8000/api/v1/register/
Content-Type: application/json

{
    "username": "username",
    "email": "user@example.com",
    "password": "yourpassword",
    "password_confirm": "yourpassword"
}
```
После успешной регистрации вы получите письмо на указанный адрес со ссылкой для активации аккаунта. Необходимо перейти по этой ссылке для завершения процесса регистрации.

### Для получение access token

```bash

POST http://localhost:8000/api/v1/login/
Content-Type: application/json

{
    "username": "yourusername",
    "password": "yourpassword"
}
```

## Работа с продуктами
1. Создание категории продукта чтобы создать новую категорию, отправьте POST-запрос:
   ```bash
   
   POST http://localhost:8000/api/v1/categories/
   Content-Type: application/json
   
   {
       "name": "Category Name",
   }
   ```

2. Создание продукта
    Чтобы создать новый продукт, отправьте POST-запрос:
   
   ```bash

   POST http://localhost:8000/api/v1/products/
   Content-Type: application/json
   
   {
       "name": "Product Name",
       "description": "Product Description",
       "price": 10.99,
       "category_id": 1,
       "image": "url_to_image"
   }
   ```

3. Обновление продукта
Чтобы обновить продукт, отправьте PUT-запрос:

   ```bash

   PUT http://localhost:8000/api/v1/products/{product_id}/
   Content-Type: application/json
   
   {
       "name": "Updated Product Name",
       "description": "Updated Description",
       "price": 12.99,
       "category_id": 2
   }
   ```

4. Получение списка продуктов
Для получения списка продуктов отправьте GET-запрос:

   ```bash
   GET http://localhost:8000/api/v1/products/
   ```
   
###  Полнотекстовый поиск продуктов
   Для поиска продуктов по тексту, отправьте GET-запрос на следующий URL:
   ```bash
   GET http://localhost:8000/api/v1/products/q="text"
   ```
## Полнотекстовый поиск продуктов и фильтрации по категориям
### Пример:
   ```bash
   curl -X GET "http://localhost:8000/api/v1/products/q=apple"
   ```
### 2. Фильтрация продуктов по категории
   Для фильтрации продуктов по категории, используйте следующий URL:
   ```bash
   GET http://localhost:8000/api/v1/products/?filter=id
   ```
### Пример:
   ```bash
   curl -X GET "http://localhost:8000/api/v1/products/?filter=category_id"
   ```

## Swagger
1. После запуска проекта, Swagger UI будет доступен по следующему адресу:

  ```bash
  http://localhost:8000/swagger/
  ```

