# docker-compose exec gets us into our backend so we can run commands.
docker-compose exec backend sh

# Then you can run:
python manage.py makemigrations profiles_app

# Will execute all of our migrations in our project.
# It will create all of the tables based on your models, and handle the dependencies.
# I think dependencies are due to some tables needing others to exist first prior to being created.
python manage.py migrate
