from django import forms
from .models import Todo

class CreateTodoForm(forms.ModelForm):
    """To-do creation form."""
    
    created_at = forms.DateTimeField(
        widget=forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'})
    )
    
    class Meta:
        model = Todo
        exclude = ('author', 'is_done', 'available',)
        
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(
                    attrs={'class': 'form-control', 'style':'min-height:140px; max-height:140px'}),
            }
        
class EditTodoForm(forms.ModelForm):
    """To-do update form."""
    
    class Meta:
        model = Todo
        exclude = ('author', 'available',)
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'style':'min-height:140px; max-height:140px'}),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }