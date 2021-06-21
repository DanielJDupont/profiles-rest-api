from django.contrib import admin

# We need to import our models to register with our admin.
from profiles_app import models

# We will register our UserProfile model.
admin.site.register(models.UserProfile)
