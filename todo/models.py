from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Todo(models.Model):
    """Model representing a to-do item."""
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created_at',)
    
    def __str__(self):
        return self.title.title()
    
    def is_available(self):
        """Check if the to-do item is available and update user's score if completed.

        If the task is marked as done and is available, the author's profile score
        is incremented by 100, and availability is set to False.

        Returns:
            bool: True if the task is still available, otherwise False.
        """
        # If the task is completed
        if self.is_done:
            if self.available:
                self.author.profile.score += 100
                self.author.profile.save()
                self.available = False
            return self.available
        else:
            return self.available
    
    def get_absolute_url(self):
        """Return the URL for the to-do detail view."""
        return reverse('todo:detail', args=[self.id])
    
    def get_edit_url(self):
        """Return the URL for the to-do edit view."""
        return reverse('todo:edit', args=[self.id])
    
    def get_delete_url(self):
        """Return the URL for the to-do delete view."""
        return reverse('todo:delete', args=[self.id])