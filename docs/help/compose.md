
# Using docker-compose

## Overview

You can use the `docker-compose.yml` associated with this image to have more 
advanced control on his usage. See the contents of the docker-compose.yml file 
to familiarize yourself with its features.

*The `docker-compose` command is an powerfull member of the Docker system and 
is highly recommended that you know his documentation: 
<https://docs.docker.com/compose/>*

## Quick Start

### Create a Docker volume to store permanent data

``` sh
docker volume create --name=daspanel-data
```

### Start container:

``` sh
docker-compose up
```

This will start an new docker container using 
`daspanel/python2.7-gunicorn` as base image. 
[?](https://docs.docker.com/compose/reference/up/)

### Stop container:

``` sh
docker-compose stop
```

Stop the running conatiner create before with the `docker-compose up` command. 
[?](https://docs.docker.com/compose/reference/stop/)

Using `stop` don't remove the created containers. If you want stop and remove 
the containers use:

``` sh
docker-compose down
```

### Remove stoped containers:

``` sh
docker-compose rm
```

Use this command to remove stopped containers create before with the 
`docker-compose up` command. 
[?](https://docs.docker.com/compose/reference/rm/)  

## Another usages

### Shell access to the container

In order to run the container and get access to a shell on it you can do:

``` sh
docker-compose run daspanel-python2.7-gunicorn /bin/sh
```

where `daspanel-python2.7-gunicorn` must be one of the 
definied services in your `docker-compose.yml`. See below relevant content of 
the compose file:
``` yaml
version: '2'
services:
    daspanel-python2.7-gunicorn:
        build:
            context: .
            dockerfile: Dockerfile
        ...
```

If you want to access the shell of an container started before use this command:

``` sh
docker exec -ti python2.7-gunicorn-python2.7-gunicorn_1 /bin/sh
```
You can get the name of the running container's using:

``` sh
docker ps -a
```

## Customization

The sample `docker-compose.yml` file in this project it's only an start point for 
your convenience. Fell free to change it for your specific needs.



