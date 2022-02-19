# country_services
Services for all cities in countries around the world such as restaurants, hotels, and others


I following in this project the <a class="reference external" href="https://github.com/HackSoftware/Django-Styleguide"> django style guide</a> 


## :triangular_flag_on_post: Features

- Django 3.0.9
- Django Rest
- all auth

### 🏠 [Homepage](https://github.com/jefftriplett/django-jobs)

## :wrench: Install

```shell
# Clone the repo
$ git clone https://github.com/jefftriplett/django-jobs/

# Change directory
$ cd django-jobs

# Rename the sample.env file to .env
$ mv sample.env .env
```

Create a virtual environment

## :rocket: Usage

```shell
# Run Django in background mode
$ docker-compose up -d

# Run Migrations
$ docker-compose run --rm web python manage.py migrate

# Run the server on http://localhost:8000/
$ docker-compose run --rm web python manage.py runserver

# Stop all running containers
$ docker-compose down

# Run Tests
$ docker-compose run --rm web pytest
```

## Show your support

Give a ⭐️ if this project helped you!
