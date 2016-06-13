FROM python:2.7.11

RUN pip install ncclient==0.4.7 && pip install pyang==1.6

WORKDIR /bin

COPY bin /bin
COPY cmd.sh / 

CMD ["python", "./netconf.py"]

