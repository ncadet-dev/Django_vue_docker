To use the application, simply have Docker installed and running on your machine and excute the below at the root of the project.

# Build the docker containers

```docker-compose build```

# Launch the built containers

```docker-compose up```

# Obtain the docker IDs
There should be two containers : one for django and one for Vue
```docker ps```

# Make migrations to set up/initialise the database
Requires the django container ID
```docker exec -it {django_container_id} python manage.py migrate```


# Create a super user in Django
This step is necessary to have access to the private route which requires login. Besides, the migrations must be made at least a first time for users to be created.

```docker exec -it {django_container_id} python manage.py createsuperuser```