FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "sh", "-c" "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000" ]