from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import Profile


def profile_save(sender, **kwargs):
    """Create a profile instance for a newly created user."""
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        


post_save.connect(receiver=profile_save, sender=User)