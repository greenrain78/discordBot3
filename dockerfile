FROM python:3.7

RUN mkdir /erbs

COPY requirements.txt /erbs
WORKDIR /erbs

RUN pip install -r requirements.txt

CMD ["python", "/discord/main.py"]