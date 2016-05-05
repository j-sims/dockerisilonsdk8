FROM ubuntu:15.04
MAINTAINER noone@nowhere.com

LABEL Description="Build an ubuntu image for testing the Isilon API SDK for OneFS 8.0 (Python)"

RUN apt-get -y update && apt-get -y install python python-setuptools wget vim git python-pip
RUN pip install urllib3 six certifi
RUN mkdir /app
ADD run.py /app
WORKDIR /app
run git clone https://github.com/Isilon/isilon_sdk_8_0_python.git
run ln -s /app/isilon_sdk_8_0_python/isi_sdk /app/
CMD ["python", "/app/run.py"]
