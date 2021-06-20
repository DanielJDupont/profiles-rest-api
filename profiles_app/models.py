from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Each model maps to a specific table in our database.
# Let's create our first models for our project.
# Note that a superuser has access to every model/table in the database in our django admin.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles."""

    def create_user(self, email, name, password=None):
        """Create a new user profile."""
        if not email:
            raise ValueError("Users must have a valid email address.")

        # Makes the right side of the email all the same.
        # The left half could be case sensitive depending on the email provider.
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # The password should be converted to a hash, that way attackers can only see the hash.
        user.set_password(password)
        # Save the user data to our database.
        user.save(using=self._db)

        # Return the newly created user object.
        return user

    # Same as above but with superuser status.
    def create_superuser(self, email, name, password):
        """Create a new superuser with given details."""
        # Self is passed in for any class functions automatically.
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system."""

    # All email fields must have a max_length specified.
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # By default users are not staff members (staff have access to admin).
    is_staff = models.BooleanField(default=False)

    # We need to tell django how to create new users.
    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Retrieve full name of user."""
        return self.name

    # We made the name field very simplistic so just return name for now.
    def get_short_name(self):
        """Retrieve shorter name of the user."""
        return self.name

    # This is great to do, so we have something to see with print() statements or in django admin.
    def __str__(self):
        """Return string representation of the user."""
        return self.email
