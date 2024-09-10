FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get -y update
RUN apt-get -y install vim

#RUN apt-get -y install libmysqlclient-dev
#
#RUN apt-get install mysql-client-core-5.6

#RUN apt-get -y install python3.10-dev

#RUN apt-get install gcc -y
#RUN mkdir /payhere
#
#ENV DOCKERIZE_VERSION v0.6.1
#RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz



ADD . /memo
#ADD ../requirements.txt /app

WORKDIR /memo
#ADD requirements.txt /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

#ENTRYPOINT ["dockerize", "-wait", "tcp://mysql:3306", "-timeout", "20s"]
#RUN dockerize -wait tcp://mysql:3306 -timeout 20s
#RUN python manage.py makemigrations
#RUN python manage.py migrate
#RUN python manage.py runserver
