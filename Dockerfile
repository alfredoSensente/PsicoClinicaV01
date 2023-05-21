FROM python:3.11.1

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

WORKDIR /app/psychoclinic

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]