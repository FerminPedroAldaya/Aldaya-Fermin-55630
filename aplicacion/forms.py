from django import forms
from .models import MensajeContacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

#SECCION DE FORM PARA QUE NO SE EXTIENDA EL VIEW Y SEA MAS LEGIBLE
#A TRAVES DE WIDGET Y LOS ATRIBUTOS SE EDITAN LA VISTA DE LOS FORMULARIOS
class EmpleadoForm(forms.Form, ):
    nombre = forms.CharField(max_length=50, required=True, 
                             label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su nombre'}))
    apellido = forms.CharField(max_length=50, required=True, 
                                label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su apellido'}))
    mail = forms.EmailField(max_length=50, required=True, 
                                label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su mail'}))
    presentacion = forms.CharField(max_length=256,required=True,label='',widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                                      'placeholder': 'Ingrese su presentación',
                                                                                                      'style': 'height: 10rem; resize: vertical;'}))
    experiencia = forms.CharField(max_length=256,required=True,label='',widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                                      'placeholder': 'Ingrese su experiencia',
                                                                                                      'style': 'height: 10rem; resize: vertical;'}))
    estudios = forms.CharField(max_length=256,required=True,label='',widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                                      'placeholder': 'Ingrese sus estudios',
                                                                                                      'style': 'height: 10rem; resize: vertical;'}))
    

class TrabajoForm(forms.Form, ):
    cargo = forms.CharField(max_length=50, required=True, 
                             label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese el cargo'}))
    detalles = forms.CharField(max_length=256,required=True,label='',widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                                      'placeholder': 'Ingrese los detalles',
                                                                                                      'style': 'height: 10rem; resize: vertical;'}))
    ubicacion = forms.CharField(max_length=50, required=True, 
                                   label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese la ubicacion'}))
    sueldo = forms.CharField(max_length=50, required=True, 
                                  label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese el sueldo'}))
    
class EmpleadorForm(forms.Form, ):
    nombre = forms.CharField(max_length=50, required=True, 
                             label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su nombre'}))
    apellido = forms.CharField(max_length=50, required=True, 
                                label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su apellido'}))
    mail = forms.EmailField(max_length=50, required=True, 
                                label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su mail'}))
    edad = forms.IntegerField(required=True, 
                                   label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su edad'}))
    profesion = forms.CharField(max_length=50, required=True, 
                                  label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su profesion'}))
    nombreEmpresa = forms.CharField(max_length=50, required=True, 
                                label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese el nombre de la empresa'}))
    presentacion = forms.CharField(max_length=256,required=True,label='',widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                                      'placeholder': 'Ingrese su presentación',
                                                                                                      'style': 'height: 10rem; resize: vertical;'}))
    
    
class RegistroUsuariosForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un usuario'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese una contraseña'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme una contraseña'}))

    class Meta:
        model = User
        fields  = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme su contraseña'}))
    first_name = forms.CharField(label="", max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
    last_name = forms.CharField(max_length=50, required=False, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

class InformacionForm(forms.Form):
    informacion = forms.CharField(max_length=256,required=True,label='',widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                                      'placeholder': 'Ingrese su informacion',
                                                                                                      'style': 'height: 10rem; resize: vertical;'}))
    

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un usuario'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))

    class Meta:
        model = User
        fields  = ['username','password']

class MensajeContactoForm(forms.ModelForm):
    asunto = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el asunto'}))
    mensaje = forms.CharField(max_length=256,required=True,label='',widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                                      'placeholder': 'Ingrese su mensaje',
                                                                                                      'style': 'height: 10rem; resize: vertical;'}))
    class Meta:
        model = MensajeContacto
        fields = [ 'asunto', 'mensaje']
    
    





