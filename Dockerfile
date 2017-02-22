FROM ubuntu:15.04
MAINTAINER noone@nowhere.com

LABEL Description="Build an ubuntu image for testing the Isilon API SDK for OneFS 8.0 (Python)"

RUN apt-get -y update && apt-get -y install python python-setuptools wget vim git python-pip
RUN pip install urllib3 six certifi
RUN mkdir /app
ADD run.py /app
WORKDIR /app
RUN pip install isi_sdk_8_0_1
RUN echo "import rlcompleter, readline" >> /root/.pythonrc
RUN echo "readline.parse_and_bind('tab:complete')" >> /root/.pythonrc
RUN echo "export PYTHONSTARTUP=~/.pythonrc" >> ~/.bashrc
CMD ["python", "/app/run.py"]
