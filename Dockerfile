FROM python:3.7.1

COPY . /home/

WORKDIR /home/
RUN python setup.py install

CMD ["sds"]
