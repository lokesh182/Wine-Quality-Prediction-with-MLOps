FROM python:3.9-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app


COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]