from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
         model = Board
         fields = ['name','description ','owner',' members ','created_at','updated_at ']
         widgets = {
             'Board': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User_id name'}),
            
}