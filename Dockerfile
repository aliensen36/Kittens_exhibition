FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app

# Копируем файл requirements.txt внутрь контейнера
COPY requirements.txt ./

# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# Устанавливаем зависимости для PostgreSQL
RUN apt-get update && apt-get install -y gcc libpq-dev
