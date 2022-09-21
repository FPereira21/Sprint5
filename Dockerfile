FROM python:latest
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN apt-get install libmariadb3 libmariadb-dev && \
    pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["python", "./main.py"]