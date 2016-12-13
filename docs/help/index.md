
# Usage


### Get
```shell
$ docker pull daspanel/python2.7-gunicorn:latest
```

### Run
```shell
$ docker run -e DASPANEL_MASTER_EMAIL=my@email.com --name=my-python2.7-gunicorn daspanel/python2.7-gunicorn:latest
```

### Stop
```shell
$ docker stop my-python2.7-gunicorn
```

### Update image
```shell
$ docker stop my-python2.7-gunicorn
$ docker pull daspanel/python2.7-gunicorn:latest
$ docker run -e DASPANEL_MASTER_EMAIL=my@email.com --name=my-python2.7-gunicorn daspanel/python2.7-gunicorn:latest
```

# Tips
