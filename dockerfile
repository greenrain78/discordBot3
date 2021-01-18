FROM python:3.7

RUN mkdir /discord

WORKDIR /discord

RUN pip install -r requirements.txt

CMD ["python", "/discord/main.py"]