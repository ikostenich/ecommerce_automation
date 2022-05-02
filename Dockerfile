FROM python:latest

RUN mkdir /automation

COPY ./ecommerce /automation/ecommerce
COPY ./requirements.txt /automation
COPY ./install_selenium.sh /automation
COPY ./pytest.ini /automation

WORKDIR /automation

RUN apt-get update
RUN pip install -r requirements.txt
RUN ["/bin/bash", "-c", "source /automation/install_selenium.sh"]
