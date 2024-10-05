
# Kittens Exhibition API

## Описание

Проект **Kittens Exhibition** предоставляет API для управления информацией о котятах, их породах, рейтингах и пользователях. Данное API поддерживает аутентификацию через JWT, а также CRUD-операции для работы с котятами и их рейтингами.

---

## Запуск с Docker

Убедитесь, что у вас установлен Docker и Docker Compose. Чтобы запустить проект с помощью Docker, выполните следующие команды:

```bash
docker-compose up --build
```

Это команда создаст и запустит контейнеры для проекта и базы данных PostgreSQL.

## Зависимости и требования

Проект использует следующие зависимости:

```txt
asgiref==3.8.1
attrs==24.2.0
colorama==0.4.6
Django==5.1.1
django-extensions==3.2.3
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
drf-spectacular==0.27.2
inflection==0.5.1
iniconfig==2.0.0
jsonschema==4.23.0
jsonschema-specifications==2023.12.1
packaging==24.1
pluggy==1.5.0
psycopg2-binary==2.9.9
PyJWT==2.9.0
pytest==8.3.3
pytest-django==4.9.0
python-dotenv==1.0.1
PyYAML==6.0.2
referencing==0.35.1
rpds-py==0.20.0
setuptools==75.1.0
sqlparse==0.5.1
tzdata==2024.2
uritemplate==4.1.1
```

---

## Аутентификация через JWT

Для использования API необходима аутентификация с помощью JWT-токенов.

### Регистрация нового пользователя и получение токенов

**Эндпоинт:** `/api/users/`

- **Метод:** POST
- **Описание:** Регистрация нового пользователя и получение JWT-токенов (access и refresh).

- **Пример запроса:**

  ```json
  {
      "username": "newuser",
      "password": "password123"
  }
  ```

- **Пример ответа:**

  ```json
  {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

После успешной регистрации можно использовать `access` токен для аутентификации в API.

---

## Документация API

Этот проект использует [Swagger UI](https://swagger.io/tools/swagger-ui/) для интерактивной документации API.

### Доступ к документации:
- **Swagger UI**: [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
- **Redoc**: [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)
- **OpenAPI схема**: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)


## Описание API с примерами

### 1. Породы котят (Breeds)

**Эндпоинт:** `/api/breeds/`

- **Метод:** GET
- **Описание:** Возвращает список доступных пород котят.

- **Пример ответа:**

  ```json
  [
      {
          "id": 1,
          "name": "Персидская"
      },
      {
          "id": 2,
          "name": "Мейн-кун"
      }
  ]
  ```

### 2. Котята (Kittens)

**Эндпоинт:** `/api/kittens/`

- **Методы:** GET, POST, PUT, DELETE
- **Описание:** Позволяет управлять данными котят (создавать, обновлять, удалять и получать информацию).

#### Получение списка котят

- **Метод:** GET
- **Пример ответа:**

  ```json
  [
      {
          "id": 1,
          "name": "Барсик",
          "color": "Серый",
          "age": 3,
          "breed": "Мейн-кун",
          "owner": 1
      },
      {
          "id": 2,
          "name": "Мурзик",
          "color": "Белый",
          "age": 2,
          "breed": "Персидская",
          "owner": 2
      }
  ]
  ```

#### Создание котенка

- **Метод:** POST
- **Пример запроса:**

  ```json
  {
      "name": "Мурка",
      "color": "Рыжий",
      "age": 4,
      "breed": 1
  }
  ```

- **Пример ответа:**

  ```json
  {
      "id": 3,
      "name": "Мурка",
      "color": "Рыжий",
      "age": 4,
      "breed": "Персидская",
      "owner": 1
  }
  ```

### 3. Рейтинги котят (Kitten Ratings)

**Эндпоинт:** `/api/kittens/<kitten_id>/ratings/`

- **Методы:** GET, POST
- **Описание:** Позволяет получить или добавить рейтинг для котенка.

#### Получение рейтингов

- **Метод:** GET
- **Пример ответа:**

  ```json
  [
      {
          "id": 1,
          "rating": 5,
          "user": 1,
          "kitten": 1
      },
      {
          "id": 2,
          "rating": 4,
          "user": 2,
          "kitten": 1
      }
  ]
  ```

#### Добавление рейтинга

- **Метод:** POST
- **Пример запроса:**

  ```json
  {
      "rating": 5
  }
  ```

- **Пример ответа:**

  ```json
  {
      "id": 3,
      "rating": 5,
      "user": 1,
      "kitten": 1
  }
  ```

### 4. Мои котята

**Эндпоинт:** `/api/kittens/my_kittens/`

- **Метод:** GET
- **Описание:** Возвращает список всех котят, добавленных текущим пользователем.

- **Пример ответа:**

  ```json
  [
      {
          "id": 1,
          "name": "Барсик",
          "color": "Серый",
          "age": 3,
          "breed": "Мейн-кун"
      }
  ]
  ```

---

## Тестирование

Для запуска тестов выполните команду:

```bash
pytest
```

Проект использует `pytest` для тестирования.
```
