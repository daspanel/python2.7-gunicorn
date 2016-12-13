
# Python2.7 Gunicorn

Python 2.7 with Gunicorn app server running inside Docker container using Alpine Linux with S6 Overlay init system.

* Free software: MIT license
* Documentation: <https://github.com/daspanel/python2.7-gunicorn/blob/master/docs/index.md> or <https://daspanel.github.io/python2.7-gunicorn>

## Environment variables
| Variable | Optional      | Example Value | Purpose
|----------|---------------|---------------|---------------|
| DASPANEL_GUUID | yes | ksdf09832klsdfkjsdlk | UUID used in Daspanel system to identify a unique instance of data. If you don't provide one Daspanel generate it using [Getuuid API](https://9jzojg54n7.execute-api.us-east-1.amazonaws.com/v1/uuid)|
| DASPANEL_MASTER_PASSWORD | yes | SomeGood#%@Passwd123 | Password to be used in the various Daspanel services. Automatically generated if you do not provide one.
| DASPANEL_MASTER_EMAIL | no | your@email.com | Email of the owner of Daspanel instance. It can be used for receiving notifications from the system. The Docker container will not run if it is not informed.

You can find the value of variables automatically generated by examining the 
container log after it starts. Or looking at the output of the console where 
you run your docker.

## How to use
Get
```shell
docker pull daspanel/python2.7-gunicorn:latest
```

Run
```shell
docker run -e DASPANEL_MASTER_EMAIL=my@email.com daspanel/python2.7-gunicorn:latest
```

## Features

* Alpine 3.4 Linux with S6 overlay
* Ssmtp to send emails using external smtp server
* Python 2.7 with pip
* Gunicorn with setproctitle gevent
* pyCurl with SSL using openssl

## Additional docs and credits

* [Project home page](https://daspanel.github.io/python2.7-gunicorn)
