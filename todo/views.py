from django.shortcuts import render, redirect, get_object_or_404
from django.views import View 
from accounts.forms import LoginForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from .models import Todo
from .forms import (
    CreateTodoForm,
    EditTodoForm,
)

class HomeView(View):
    """Display the home page for both anonymous and authenticated users."""
    template_name = 'todo/home.html'
    
    def get(self, request):
        """Render the home page with the user's tasks if authenticated."""
        if request.user.is_authenticated:
            todos = Todo.objects.filter(author=request.user).order_by('is_done')
            context = {'todos':todos}
        else:
            context = {}
        return render(request, self.template_name, context)
    
    
    
class CreateTodoView(LoginRequiredMixin, View):
    """Create a new To-do item for the authenticated user."""
    template_name = 'todo/create.html'
    form_class = CreateTodoForm
    
    def get(self, request):
        """Render to-do creation form."""
        form = self.form_class(initial={
            'created_at':timezone.now(),
        })
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        """Create a new to-do item with submitted data."""
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            todo = Todo.objects.create(
                author=request.user,
                title=cd['title'],
                description=cd['description'],
            )
            messages.success(request, "Your new task has been created successfully.")
            return redirect('todo:home')
        
        return render(request, self.template_name, {'form':form})
    
    
    
class DetailTodoView(LoginRequiredMixin, View):
    """Display the details of a specific to-do item for the authenticated user."""
    template_name = 'todo/detail.html'
    
    def get(self, request, pk):
        """Render to-do detail form."""
        todo = get_object_or_404(Todo, pk=pk)
        if request.user != todo.author:
            messages.error(request, "You are not the author.", 'danger')
            return redirect('todo:home')
        
        todo_created_at = todo.created_at.strftime('%Y-%m-%d')
        
        return render(request, self.template_name, {'todo':todo, 'todo_created_at':todo_created_at})
            
    

    
class EditTodoView(LoginRequiredMixin, View):
    """Update an existing To-do item for the authenticated user."""
    template_name = 'todo/edit.html'
    form_class = EditTodoForm
    
    def setup(self, request, *args, **kwargs):
        """Initialize the to-do instance."""
        self.todo_instance = get_object_or_404(Todo, pk=kwargs['pk'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request ,*args, **kwargs):
        """Ensure the user is authorized to edit the to-do item."""
        if request.user != self.todo_instance.author:
            messages.error(request, "You are not authorized to edit this task.", 'danger')
            return redirect('todo:home')
        
        if not self.todo_instance.is_available():
            messages.warning(request, "This task is already finished.")
            return redirect('todo:home')
        
        
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk):
        """Render the edit form for to-do item."""
        form = self.form_class(instance=self.todo_instance)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, pk):
        """Update the to-do item with submitted data."""
        
        form = self.form_class(data=request.POST, instance=self.todo_instance)
        if form.is_valid():
            cd = form.cleaned_data
            self.todo_instance.title = cd['title']
            self.todo_instance.description = cd['description']
            self.todo_instance.is_done = cd['is_done']
            self.todo_instance.save()
            
            # Each time the user completes a task, they earn 100 points
            if self.todo_instance.is_done:
                text = "Congratulations! You have earned +100 points for completing the task."
                messages.success(request, text)
                
            messages.success(request, "Your task has been updated successfully.")
            return redirect('todo:home')
        
        return render(request, self.template_name, {'form':form})


    
class DeleteTodoView(LoginRequiredMixin, View):
    """Delete a specific To-do item for the authenticated user."""
    template_name = 'todo/delete.html'
    
    def setup(self, request, *args, **kwargs):
        """Initialize the to-do instance for deletion."""
        self.todo_instance = get_object_or_404(Todo, pk=kwargs['pk'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        """Ensure the user is authorized to delete the to-do item."""
        if request.user != self.todo_instance.author:
            messages.error(request, "You are not authorized to delete this task.", 'danger')
            return redirect('todo:home')
        
        
        return super().dispatch(request, *args, **kwargs)
        
    
    def get(self, request, pk):
        """Render the confirmation page for to-do deletion."""
        return render(request, self.template_name, {'pk':pk})
    
    def post(self, request, pk):
        """Delete the to-do item and redirect to the home page."""
        messages.success(request, "The task has been deleted successfully.")
        self.todo_instance.delete()
        return redirect('todo:home')
        