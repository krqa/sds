FROM python:3.7.1

COPY . /home/

WORKDIR /home/
RUN python setup.py install

RUN mkdir /output/
WORKDIR /output/

VOLUME ["/output/"]

ENTRYPOINT ["sds"]
