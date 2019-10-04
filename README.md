[![Build Status](https://travis-ci.org/sunscrapers/flask-boilerplate.svg?branch=master)](https://travis-ci.org/sunscrapers/flask-boilerplate)

# Basic Flask App Server (may contain data models)

This repository contains a sample minimal Flask application structure that includes:

* SQLAlchemy (using Postgresql)
* Alembic
* Flask
* Celery (coming soon)
* py.test
* Swagger

It runs on Python 3.5+.

## Installation

First, clone the repository and create a virtualenv: 

`$ make init`

Then install the requirements:


`$ make update_deps`

Before running the application make sure that your local PostgreSQL server is up. Then create the databases:

```
$ CREATE DATABASE dogear;
$ CREATE DATABASE dogear_test;
```

Now you can create the tables using Alembic:

`$ make upgrade`

Finally you can run the application:

`$ make run`

or play in the Python REPL:

`$ python manage.py shell`

In order to run unit tests in py.test invoke:

`$ make test`



#TODO
DO hosting:
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

Fabistrano:
https://github.com/dlapiduz/fabistrano
