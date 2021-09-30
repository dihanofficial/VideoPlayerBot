FROM python:latest
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN apt-get install ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
COPY . /py
WORKDIR /py
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt
CMD python3 -m bot
