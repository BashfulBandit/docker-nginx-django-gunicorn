# Django based website using Docker, NGINX, Gunicorn, and MariaDB.

With this repo you will be able to set up a Nginx, Django/Gunicorn, and MariaDB
to develop and deploy a Django website.

## Prerequisites

In order to use this compose file (docker-compose.yml) you must have:

1. docker (https://docs.docker.com/engine/installation/)
2. docker-compose (https://docs.docker.com/compose/install/)

## How to use it

1. Clone this repository

```
$ git clone https://github.com/BashfulBandit/docker-nginx-django-gunicorn.git
```

2. Run the start.sh

```
$ bash bin/start.sh
```

You can now see your Django website running at http://localhost:8000.

3. Stop the services.

```
$ bash bin/stop.sh
```

## Docker Images

* [dtempleton/django](https://hub.docker.com/r/dtempleton/django/)
* [nginx](https://hub.docker.com/_/nginx/)
* [mariadb](https://hub.docker.com/_/mariadb/)

While I use MariaDB as my Database of choice, you should be able to use any Django
supported database management system. See the Docker Hub page for the
dtempleton/django Docker image for how it uses environment variables to define
some Django variables in settings.py.
