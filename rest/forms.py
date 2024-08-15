from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm 
from .models import Menu, Category, Take, Booking, Contact
from django import forms

# forms.py


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['category', 'name', 'price', 'description', 'image']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'input',
                'id': 'category',
                'placeholder': 'Type or select a fruit'
            }),
            'name': forms.TextInput(attrs={
                'class': 'input',
                'id': 'cated',
                'placeholder': 'Menu Name',
                'required': True
            }),
            'price': forms.NumberInput(attrs={
                'class': 'input',
                'id': 'price',
                'placeholder': 'Enter Price'
            }),
            'description': forms.Textarea(attrs={
                'class': 'input',
                'rows': 4,
                'cols': 50,
                'placeholder': 'Menu Description',
                'required': True
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'input',
                'accept': 'image/*'
            }),
        }

class CategoryForm(ModelForm):
    class Meta: 
        model = Category 
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'id': 'cated',
                'placeholder': 'Category Name',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'input',
                'id': 'description',
                'placeholder': 'Description',
                'rows': 4,
                'cols': 50,
                'required': True,
            }),
        }
       
class TakeForm(ModelForm):
    class Meta: 
        model = Take 
        fields = '__all__'
        
class BookingForm(ModelForm):
    class Meta: 
        model = Booking 
        fields = '__all__'
        
        





class CustomUserCreationForm(UserCreationForm):
    is_superuser = forms.BooleanField(
        required=False, 
        label='Superuser Status',
        widget=forms.CheckboxInput(attrs={
            'class': 'input',
            'id': 'superuser'
        })
    )

    class Meta:
       
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input',
                'id': 'cated',
                'placeholder': 'UserName',
            }),
            'password': forms.TextInput(attrs={
                'class': 'input',
                'id': 'password',
                'placeholder': 'Password',
            }),
            'password2': forms.TextInput(attrs={
                'class': 'input',
                'id': 'confirm_password',
                'placeholder': 'Confirm Password',
            }),
        }
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
        # Adding widgets to customize the form fields
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'E-mail',
                'id': 'email',
                'required': True,
            }),
            'message': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Message',
                'id': 'message',
                'required': True,
            }),
            
        }