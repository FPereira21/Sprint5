FROM python:latest
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY wait-fot-it.sh wait-for-it.sh

CMD ["wait-for-it.sh" ,"db:5432" ,"python", "./main.py"]