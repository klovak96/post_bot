FROM python:latest

# Установим рабочую директорию
WORKDIR /app

# Копируем файлы проекта (замените на ваши файлы)
COPY . /app/

# Копируем requirements.txt
COPY requirements.txt /app/

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска вашего бота (замените на команду запуска вашего скрипта)
CMD ["python", "pbot.py"]