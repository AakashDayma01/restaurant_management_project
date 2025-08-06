from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Extends the default Django User model to store additional user profile information,
    including full name, email, and phone number.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=225)
    phone_number = moodels.CharField(max_length=15)

    def __str__(self):
        return self.user.get_full_name() or self.name