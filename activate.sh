# Activate the python virutal environment in .pyvenv.
source .pyvenv/bin/activate

# Note that you will need to use python manage.py instead of django-admin once you have created your project.
# You can create new apps using the python manage.py commands.


# Note that we have to sometimes perform things like migrations inside of our docker container.
# We can get inside of it with an exec command.
# docker-compose exec, is the command itself we want.
# backend, is the name of the service in the docker-compose.yml we want to enter.
# sh, we want to enter the backend in sh mode.
docker-compose exec backend sh

# use the web service:
docker-compose exec web sh

python3 manage.py migrate


docker-compose up --build


# If on linux, you will not have permissions to several files.
# You will have to run this command to change that.
sudo chown -R $USER:$USER .

# Permissions issues?
# https://docs.docker.com/samples/django/
