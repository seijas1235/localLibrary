from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFormStaf(UserCreationForm):
    email=forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'password1', 'password2','is_staff')
    
    
    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este Correo ya existe, Ingresa Otro.")
        return email



class UserCreationFormWithEmail(UserCreationForm):
    email=forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'password1', 'password2')
    
    
    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este Correo ya existe, Ingresa Otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields =['image','cui','direccion','zona','date_of_birth','municipio','escolaridad','genre','colegio']

        widgets={
            'image' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'cui' : forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'DPI'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Direccion'}),
            'zona' : forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Zona'}),
            'date_of_birth' : forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Fecha de Nacimiento','type':'date'}),
            'municipio' : forms.Select(attrs={'class':'form-control mt-3', 'placeholder':'Municipio'}),
            'escolaridad' : forms.Select(attrs={'class':'form-control mt-3', 'placeholder':'Escolaridad'}),
            'genre' : forms.Select(attrs={'class':'form-control mt-3', 'placeholder':'Genero'}),
            'colegio' : forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Institucion Educativa'}),
            
        }