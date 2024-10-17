from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    """Extends the default User model to include additional profile information."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username