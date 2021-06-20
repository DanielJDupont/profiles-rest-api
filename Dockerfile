# This container will learn python, docker will install everything needed for python.
FROM python:3.9
# Allows us to see logs in the docker container.
ENV PYTHONUNBUFFERED 1
# Can be named anything.
WORKDIR /project

# Put our requirements into the docker container.
COPY requirements.txt /project/requirements.txt
RUN pip install -r requirements.txt

# Copy all of your files into the docker container.
COPY . /project

# The localhost of the docker container is indicated by 0.0.0.0.
CMD python manage.py runserver 0.0.0.0:8000
