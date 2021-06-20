from django.db import models

# These are the base classes for customizing the base model.
# Check teh documentation.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Ensures 2 spaces below classes according to PEP guidelines.
# BaseUserManager is a parent class.
# Raise an error to the user.
# Make sure the password is converted to a hash.
# Users may be able to see the hashed passwords.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles."""

    def create_user(self, email, name, password=None):
        """Create a new user profile."""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # Use the built in security of set_password supported by Django.
        # The standard is the sepcify the one of many databases you want to use.
        # You do not need to do this, but you really should in case you choose to support multiple databases in the future.
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_super_user(self, email, name, password):
        """Create and save a new superuser with given details."""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Inherit from the abstract base user to get the entire user.
# Inherit the permissions system as well.
# Use triple quotes to docstring for every class or function.
# A staff user has access to the Django admin panel.
# We need to specify the model manager as well, to use our django cli.
# It needs to know how to create and control users.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # We have not made this yet.
    objects = UserProfileManager()

    # We want email and password, not username and password, overwrite the built in username field from our abstract base user.
    # They must specify their email (default required) and we want a name as well.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    # The follow
    def get_full_name(self):
        """Retrieve full name of user."""
        return self.name

    def get_short_name(self):
        """Retrieve shortened name of user."""
        return self.name

    # It is advised to do this for all models so you can get something useful out of print() statements for this model.
    def __str__(self):
        """Return the string representation of our user."""
        return self.email


# Create your models here.
# Create superuser command is provided by the django cli to add superusers to the system.
# A superuser has full control and can see all values in the database.
# When it creates a user it expects a username and password field.
