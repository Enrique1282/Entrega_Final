from django.shortcuts import render
from .models import Estilos, Ingredientes, User, Imagen, ResenaCerveza
from .forms import (BuscaEstilo, EstiloFormulario, MyUserEditForm,
                     FormularioResenaCerveza, UserRegisterform, IngredientesForm)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Categoria, Tema, Mensaje
from .forms import NuevoMensajeForm



def inicio(request):
   
    return render(request, "Appfinal/index2.html")
@login_required
def inicio2(request):
   
    return render(request, "Appfinal/index.html")

@login_required
def about(request):
   
    return render(request, "Appfinal/aboutme.html")

@login_required
def cargar_estilo(request):

    if request.method == 'POST':
        estilo = Estilos(nombre=request.POST['nombre'],
                      color=request.POST['color'], amargor=request.POST['amargor'],
                      descripcion=request.POST['descripcion'])
        estilo.save()

        return render(request, "Appfinal/index.html")

    return render(request, "Appfinal/cargar_estilo.html")

@login_required
def cargar_ingredientes(request):
    if request.method == 'POST':
        estilo = request.POST.get('estilo', '')
        malta = request.POST.get('malta', '')
        lupulo = request.POST.get('lupulo', '')
        levadura = request.POST.get('levadura', '')
        descripcion = request.POST.get('descripcion', '')
       
        ingredientes = Ingredientes(
            estilo=estilo,
            malta=malta,
            lupulo=lupulo,
            levadura=levadura,
            descripcion=descripcion
        )
        if request.user.is_authenticated:
            ingredientes.author = request.user
        else:
            ingredientes.author = None
        ingredientes.save()

        return render(request, "Appfinal/index.html")

    return render(request, "Appfinal/cargar_ingredientes.html")

@login_required
def listar_ingredientes(request):

    ingredientes = Ingredientes.objects.all()  # trae todos los cursos

    contexto = {"ingredientes": ingredientes}

    return render(request, "Appfinal/listarIngredientes.html", contexto)

def delete_ingrediente(request, ingrediente_id):

    ingrediente = Ingredientes.objects.get(id=int(ingrediente_id))
    ingrediente.delete()

    # vuelvo al menú
    ingrediente = Ingredientes.objects.all()  # trae todos los cursos
    return render(request, "Appfinal/listarIngredientes.html", {"ingredientes": ingrediente})

def edit_ingrediente(request, ingrediente_id):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = IngredientesForm(request.POST, request.FILES)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            ingrediente = Ingredientes.objects.get(id=ingrediente_id)
            ingrediente.malta = informacion["malta"]
            ingrediente.lupulo = informacion["lupulo"]
            ingrediente.levadura = informacion["levadura"]
            ingrediente.descripcion = informacion["descripcion"]
            ingrediente.save()

            return render(request, "Appfinal/index.html")
    else:
        ingrediente = Ingredientes.objects.get(id=ingrediente_id)
        miFormulario = IngredientesForm(
            initial={"malta": ingrediente.malta, "lupulo": ingrediente.lupulo, "levadura": ingrediente.levadura,
                     "descripcion": ingrediente.descripcion})

    return render(request, "Appfinal/editar_estilo.html", {"miFormulario": miFormulario})

@login_required
def buscar_estilo(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = BuscaEstilo(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            estilos = Estilos.objects.filter(
                nombre__icontains=informacion["estilo"])

            if estilos:
                return render(request, "Appfinal/lista.html", {"estilos": estilos})
            else:
                mensaje = "Estilo no encontrado"
                return render(request, "Appfinal/lista.html", {"mensaje": mensaje})
    else:
        miFormulario = BuscaEstilo()

    return render(request, "Appfinal/ver_estilos.html", {"miFormulario": miFormulario})

@login_required
def ipa(request):
    return render(request, "Appfinal/ipa.html")

@login_required
def scotish(request):
    return render(request, "Appfinal/scotish.html")

@login_required
def golden(request):
    return render(request, "Appfinal/golden.html")

@login_required
def apa(request):
    return render(request, "Appfinal/apa.html")

@login_required
def blog(request):
    return render(request, "Appfinal/blog.html")

@login_required
def nosotros(request):
    return render(request, "Appfinal/nosotros.html")

@login_required
def ver_BD(request):

    estilos = Estilos.objects.all()  # trae todos los cursos

    contexto = {"estilos": estilos}

    return render(request, "Appfinal/leer_BD.html", contexto)

def delete_estilo(request, estilo_id):

    estilo = Estilos.objects.get(id=int(estilo_id))
    estilo.delete()

    # vuelvo al menú
    estilo = Estilos.objects.all()  # trae todos los cursos
    return render(request, "Appfinal/leer_BD.html", {"estilos": estilo})

def edit_estilo(request, estilo_id):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = EstiloFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            estilo = Estilos.objects.get(id=estilo_id)
            estilo.nombre = informacion["nombre"]
            estilo.color = informacion["color"]
            estilo.amargor = informacion["amargor"]
            estilo.descripcion = informacion["descripcion"]
            estilo.save()

            return render(request, "Appfinal/index.html")
    else:
        estilo = Estilos.objects.get(id=estilo_id)
        miFormulario = EstiloFormulario(
            initial={"nombre": estilo.nombre, "color": estilo.color, "amargor": estilo.amargor,
                     "descripcion": estilo.descripcion})

    return render(request, "Appfinal/editar_estilo.html", {"miFormulario": miFormulario})

@login_required
def receta_blonde(request):
    return render(request, "Appfinal/receta_blonde.html")

@login_required
def receta_ipa(request):
    return render(request, "Appfinal/receta_ipa.html")

@login_required
def receta_porter(request):
    return render(request, "Appfinal/receta_porter.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "Appfinal/index.html", {"mensaje": f"Bienvenido/a {usuario}"})
            else:
                form = AuthenticationForm()
                return render(request, "Appfinal/login2.html", {"mensaje": "Error, datos incorrectos", "form": form})

        else:
            return render(request, "Appfinal/index2.html", {"mensaje": "Usuario o Contraseña incorrecto"})

    form = AuthenticationForm()

    return render(request, "Appfinal/login2.html", {"form": form})

def registrarse(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterform(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Appfinal/index2.html", {"mensaje": f"{username} ¡Registro exitoso!\n Ahora puedes iniciar sesión"})
    else:
        # form = UserCreationForm()
        form = UserRegisterform(request.POST)

    return render(request, "Appfinal/register2.html", {"form": form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = MyUserEditForm(request.POST, request.FILES)
        # archivo_form = AvatarForm(request.POST, request.FILES)

        if miFormulario.is_valid():  # and archivo_form.is_valid():

            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            # usuario.password1 = informacion['password1']
            # usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            # miFormulario.save()
            # perfil.avatar = archivo_form.cleaned_data["avatar"]
            # perfil.save()

            user = User.objects.get(username=request.user)
            try:
                avat = Imagen.objects.get(user=user)
            except Imagen.DoesNotExist:
                avat = Imagen(user=user, imagen=informacion.get("imagen"))
                avat.save()
            else:
                avat.imagen = miFormulario.cleaned_data["avatar"]
                avat.save()

            # archivo_form.save()

            return render(request, "Appfinal/index.html")
        else:
            miFormulario = MyUserEditForm()

    else:
        miFormulario = MyUserEditForm(
            initial={
                'email': usuario.email,
                'last_name': usuario.last_name,
                'first_name': usuario.first_name
            }
        )
    return render(request, "Appfinal/editarPerfil_2.html", {"miFormulario": miFormulario,
                                                      "usuario": usuario
                                                      }
                  )

@login_required
def ver_estilo(request, estilo_id):
    estilo =Estilos.objects.get(id=estilo_id)
    return render(request, 'Appfinal/ver_estilo.html', {'estilo': estilo})

@login_required
def agregar_resena_cerveza(request):
    if request.method == 'POST':
        form = FormularioResenaCerveza(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Appfinal/index.html")
    else:
        form = FormularioResenaCerveza()
    
    return render(request, 'Appfinal/agregar_resena_cerveza.html', {'form': form})

@login_required
def listar_resenas(request):
    resenas = ResenaCerveza.objects.all()  # Recupera todas las reseñas de la base de datos
    return render(request, 'Appfinal/listar_resenas.html', {'resenas': resenas})

def delete_resena(request, resena_id):

    resena = ResenaCerveza.objects.get(id=int(resena_id))
    resena.delete()

    # vuelvo al menú
    resena = ResenaCerveza.objects.all()  # trae todos los cursos
    return render(request, "Appfinal/listar_resenas.html", {"resenas": resena})

def edit_resena(request, resena_id):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = FormularioResenaCerveza(request.POST, request.FILES)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            resena = ResenaCerveza.objects.get(id=resena_id)
            resena.titulo = informacion["titulo"]
            resena.cerveceria = informacion["cerveceria"]
            resena.estilo = informacion["estilo"]
            resena.contenido = informacion["contenido"]
            resena.calificacion = informacion["calificacion"]
            resena.save()

            return render(request, "Appfinal/index.html")
    else:
        resena = ResenaCerveza.objects.get(id=resena_id)
        miFormulario = FormularioResenaCerveza(
            initial={"titulo": resena.titulo, "cerveceria": resena.cerveceria, "estilo": resena.estilo,
                     "contenido": resena.contenido, "calificacion": resena.calificacion})

    return render(request, "Appfinal/editarResena.html", {"miFormulario": miFormulario})

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'Appfinal/lista_categorias.html', {'categorias': categorias})

@login_required
def lista_temas(request, categoria_id):
    temas = Tema.objects.filter(categoria__id=categoria_id)
    return render(request, 'Appfinal/lista_temas.html', {'temas': temas})

@login_required
def ver_tema(request, tema_id):
   
    tema = Tema.objects.get(pk=tema_id)
    mensajes = Mensaje.objects.filter(tema=tema)
    
    if request.method == 'POST':
        form = NuevoMensajeForm(request.POST)
        if form.is_valid():
            nuevo_mensaje = form.save(commit=False)
            nuevo_mensaje.tema = tema
            nuevo_mensaje.autor = request.user  # Asumiendo que estás utilizando autenticación de usuarios.
            nuevo_mensaje.save()
            return render(request, "Appfinal/index.html")
    else:
        form = NuevoMensajeForm()

    return render(request, 'Appfinal/ver_tema.html', {'tema': tema, 'mensajes': mensajes, 'form': form})
