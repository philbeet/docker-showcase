FROM python:3.9-slim

WORKDIR /client

COPY . /client

RUN pip install -r requirements.txt

CMD ["python", "client.py"]