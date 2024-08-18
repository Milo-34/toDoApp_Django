from django import forms
from .models import Task  # Import your Task model

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'is_complete']  # Include the fields you want to edit

        # Optionally, customize widgets
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
