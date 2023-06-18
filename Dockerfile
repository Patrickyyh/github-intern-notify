FROM python:3.8.3

WORKDIR /app

ADD . /app


RUN pip install -r requirements.txt

CMD [ "python3" ,"./main.py" ]



