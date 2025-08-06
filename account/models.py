from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Extends the default Django User model to store additional user profile information,
    including full name, email, and phone number.
    """
    # Link to Django's built in user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # This field stores the name of the user
    name = models.CharField(max_length=100, blank=True)

    # This field stores the Email of the user
    email = models.EmailField(max_length=225, blank=True)

    # this field stores the Contact number of the user
    phone_number = models.CharField(max_length=15, null=True)

    def __str__(self):
        """
        Return the full name of the user if available; otherwise , fall back to the 'name' field.
        """
        full_name = self.user.get_full_name()
        return full_name if full_name else self.name
