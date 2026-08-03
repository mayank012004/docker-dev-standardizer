FROM python:3.12

WORKDIR /app

COPY ./app /app

RUN pip install django psycopg[binary]

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]