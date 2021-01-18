FROM python:3.7

RUN mkdir /discord

COPY requirements.txt /discord
WORKDIR /discord

RUN pip install -r v

CMD ["python", "/discord/main.py"]