FROM ubuntu:16.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && apt-get install -y libboost-all-dev python3-pip cmake g++
RUN apt-get install -y git

RUN git clone https://github.com/alesapin/CrossMorphy.git \
 && cd CrossMorphy/build \
 && cmake .. \
 && make

ADD requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

ADD *.py /
ENTRYPOINT ["python3", "-u", "/main.py"]
