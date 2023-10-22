from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ResenaCerveza
from .models import Tema, Mensaje, Categoria


class BuscaEstilo(forms.Form):
    estilo = forms.CharField()

class EstiloFormulario(forms.Form):
    nombre = forms.CharField()
    color = forms.CharField()
    amargor = forms.CharField()
    descripcion = forms.CharField()


class IngredientesForm(forms.Form):
    malta = forms.CharField()
    lupulo = forms.CharField()
    levadura = forms.CharField()
    descripcion = forms.CharField()

class UserRegisterform(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    # Acá se definen las opciones que queres modificar del usuario,
    # Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        # Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}

class AvatarFormulario(forms.Form):

    # Especificar los campos
    imagen = forms.ImageField(required=True)

class MyUserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput, required=False)

    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name',
                  'password1', 'password2', 'avatar']
        

class FormularioResenaCerveza(forms.ModelForm):
    class Meta:
        model = ResenaCerveza
        fields = ['titulo', 'cerveceria', 'estilo', 'contenido', 'calificacion']


class NuevoTemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'contenido']

class NuevoMensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
