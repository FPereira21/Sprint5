FROM python:latest
WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt
COPY ./main.py main.py
COPY ./wait-for-it.sh ./wait-for-it.sh
RUN pip install --no-cache-dir -r requirements.txt && \
    chmod +x ./wait-for-it.sh


CMD ["./wait-for-it.sh" ,"postgresdocker:5432" ,"--" ,"python", "./main.py"]