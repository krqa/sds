# sds

[aka. *Simple Data Standardizer*]

Downloads data in different formats from different places and outputs a standardized subset in one, common format.

## use

### run

#### with docker

*Note:* Outputed file will be *inside* the container. Container exposes a `/output/` volume, which serves as a default directory for output file.

```bash
$ docker build -t sds .
$ docker run -it sds [-o OUTPUT_FILE] <url> [url...]
```

#### manually

*Requirements*: Python3

*Probably do this from within virtualenv.*

```bash
$ python setup.py install
$ sds [-o OUTPUT_FILE] <url> [url...]
```
