FROM python:3.10.6-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

RUN mkdir -p /usr/src/RadioBot
WORKDIR /usr/src/RadioBot
COPY bot.py /usr/src/RadioBot/
COPY requirements.txt /usr/src/RadioBot/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python bot.py $BOT_TOKEN $RADIO_URL