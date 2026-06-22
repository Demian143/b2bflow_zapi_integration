FROM python:3.14

WORKDIR /code

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    libdbus-1-dev

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

RUN pip install fastapi[standard]

EXPOSE 80

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "80"]