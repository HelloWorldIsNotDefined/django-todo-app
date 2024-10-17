from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from .models import Profile
from .forms import (
    RegisterForm,
    LoginForm,
    ProfileForm,
)


class RegisterView(View):
    """Handles user registration functionality."""
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    
    def dispatch(self, request, *args, **kwargs):
        """Ensure that the authenticated user cannot access to this page."""
        if request.user.is_authenticated:
            messages.error(request, "You are already signed up.", 'danger')
            return redirect('todo:home')
            
            
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        """Render user registration form."""
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        """Create a new user."""
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                username=cd['username'],
                password=cd['password'],
            )
            messages.success(request, "Your account has been created successfully.")
            return redirect('accounts:login')
        
        return render(request, self.template_name, {'form':form})
    
    
    
class LoginView(View):
    """Handles user login functionality."""
    template_name = 'accounts/login.html'
    form_class = LoginForm
    
    def dispatch(self, request, *args, **kwargs):
        """Ensure that the authenticated user cannot access to this page."""
        if request.user.is_authenticated:
            messages.error(request, "You are already logged in.", 'danger')
            return redirect('todo:home')
            
            
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        """Render user login form."""
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        """Authenticate the user if the provided data is correct; otherwise, raise an error."""
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, 
                username=cd['username'],
                password=cd['password'],
            )
            
            if user:
                messages.success(request, "You have successfully logged in.")
                login(request, user)
                return redirect('todo:home')
            else:
                messages.error(request, "Invalid username or password. Please try again.", 'danger')
                
        return render(request, self.template_name, {'form':form})
    
    
    
class LogoutView(LoginRequiredMixin, View):
    """Handle user logout."""
    
    def get(self, request):
        """Log the user out and redirect to the home page."""
        logout(request)
        messages.success(request,"You have been logged out.")
        return redirect('todo:home')
    
    
class DeleteUserView(LoginRequiredMixin, View):
    """Handle authenticated user account deletion."""
    template_name = 'accounts/delete.html'
    
    def dispatch(self, request, *args, **kwargs):
        """Ensure that the user can delete their own account, not others."""
        user = get_object_or_404(User, pk=kwargs['pk'])
        if request.user != user:
            messages.error(request, "You are not authorized to delete this account.", 'danger')
            return redirect('todo:home')
        
        
        return super().dispatch(request, *args, **kwargs)
        
    
    def get(self, request, pk):
        """Render the account deletion confirmation page."""
        return render(request, self.template_name)
    
    def post(self, request, pk):
        """Delete the user from database."""
        request.user.delete()
        text = "Your account has been deleted successfully."
        messages.success(request, text)
        return redirect('todo:home')
    


class ProfileView(LoginRequiredMixin, View):
    """Hnadle authenticated user profile functionality."""
    template_name = 'accounts/profile.html'
    form_class = ProfileForm
    
    def setup(self, request, *args, **kwargs):
        """Initialize the user and profile instances."""
        self.user_instance = request.user
        self.profile_instance = self.user_instance.profile
        
        
        return super().setup(request, *args, **kwargs)
    
    def get(self, request):
        """Render the user profile form."""
        form = self.form_class(
            instance=self.profile_instance,
            # The initial parameter is used to instantiate the form.
            initial = {
                'first_name':self.user_instance.first_name,
                'last_name':self.user_instance.last_name,
                'email':self.user_instance.email,
            }
        )
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        """Update the user profile."""
        form = self.form_class(data=request.POST ,instance=self.profile_instance)
        if form.is_valid():
            cd = form.cleaned_data
            
            # update user instances:
            self.user_instance.first_name = cd['first_name']
            self.user_instance.last_name = cd['last_name']
            self.user_instance.email = cd['email']
            self.user_instance.save()
            
            # update profile instance
            self.profile_instance.age = cd['age']
            self.profile_instance.save()
            
            messages.success(request, "Your profile has been updated successfully.")
            
            return redirect('todo:home')
        
        return render(request, self.template_name, {'form':form})
    
    
