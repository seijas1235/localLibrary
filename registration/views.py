from .forms import UserCreationFormWithEmail, ProfileForm, UserCreationFormStaf
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.



class SingUpAdminView(CreateView):
    form_class=UserCreationFormStaf
    User.is_staff=True
    template_name='registration/signupadmin.html'

    def get_success_url(self):
        return reverse_lazy('login') +'?register'
    
    def get_form(self, form_class=None):
        form = super( SingUpAdminView, self ).get_form()
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombres'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Apellidos'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario(se usara para inicio de sesion)'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Direccion de email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar Contraseña'})
        form.fields['is_staff'].widget = forms.CheckboxInput(attrs={'class':'form-control mb-2', 'checked':'True','style':'display:none'})
        
        return form



class SingUpView(CreateView):
    form_class=UserCreationFormWithEmail
    template_name='registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') +'?register'
    
    def get_form(self, form_class=None):
        form = super( SingUpView, self ).get_form()
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombres'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Apellidos'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario (se usara para inicio de sesion)'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Direccion de email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar Contraseña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class=ProfileForm
    success_url = reverse_lazy('index') 
    template_name='registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile