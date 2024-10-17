from django.db.models.signals import pre_save
from .models import Todo

def todo_save(sender, **kwargs):
    todo = kwargs['instance']
    
    if todo.is_done:
        todo.is_available()

pre_save.connect(receiver=todo_save, sender=Todo)