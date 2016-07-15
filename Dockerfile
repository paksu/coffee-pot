FROM resin/raspberrypi-python:3.5.1

# switch on systemd init system in container
ENV INITSYSTEM on
ENV DATABASE_URL sqlite:////data/db.sqlite3

# pip install python deps from requirements.txt
# For caching until requirements.txt changes
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["bash","start.sh"]
