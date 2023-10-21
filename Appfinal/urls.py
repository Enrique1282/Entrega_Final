from django.urls import path
from Appfinal.views import (inicio, cargar_estilo, cargar_ingredientes, buscar_estilo,
                            ipa, scotish, apa, ver_BD, delete_estilo, edit_estilo, golden,
                            blog, nosotros, receta_blonde, receta_ipa, receta_porter, login_request,
                            registrarse, editarPerfil, ver_estilo, agregar_resena_cerveza,
                            listar_resenas, lista_categorias,lista_temas,ver_tema, delete_resena, 
                            edit_resena, listar_ingredientes, delete_ingrediente, edit_ingrediente
                            )
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('inicio/',  inicio, name="Inicio"),
    path('cargarEstilo/', cargar_estilo, name="CargarEstilo" ),
    path('cargarIngredientes/', cargar_ingredientes, name="CargarIngredientes" ),
    path('listarIngredientes/', listar_ingredientes, name="ListarIngredientes" ),
    path('deleteIngrediente/<int:ingrediente_id>', delete_ingrediente, name="DeleteIngrediente" ),
    path('editarIngrediente/<int:ingrediente_id>', edit_ingrediente, name="EditarIngrediente" ),
    path('buscarEstilo/', buscar_estilo, name="BuscarEstilo" ),
    path('verBD/', ver_BD, name="VerBD" ),
    path('blog/', blog, name="Blog" ),
    path('about/', nosotros, name="Nosotros" ),
    path('ipa/', ipa, name="Ipa" ),
    path('apa/', apa, name="Apa" ),
    path('scotish/', scotish, name="Scotish" ),
    path('golden/', golden, name="Golden" ),
    path('recetablonde/', receta_blonde, name="RecetaBlonde" ),
    path('recetaipa/', receta_ipa, name="RecetaIpa" ),
    path('recetaporter/', receta_porter, name="RecetaPorter" ),
    path('deleteEstilo/<int:estilo_id>', delete_estilo, name="DeleteEstilo" ),
    path('editarEstilo/<int:estilo_id>', edit_estilo, name="EditarEstilo" ),
    path('ver_estilo/<int:estilo_id>', ver_estilo, name="VerEstilo" ),
    path('agregar_resena_cerveza/', agregar_resena_cerveza, name='AgregarResenaCerveza'),
    path('listar_resenas/', listar_resenas, name='ListarResenas'),
    path('editar_resena/<int:resena_id>', edit_resena, name='EditarResena'),
    path('delete_resenas/<int:resena_id>', delete_resena, name='DeleteResena'),
]

urlpatterns += [
    path('login/', login_request, name="Login"),
    path('registrarse/', registrarse, name="Registrarse"),
    path('editarPerfil/', editarPerfil, name="EditarPerfil"),
    path('logout/', LogoutView.as_view(
        template_name='Appfinal/logout.html'), name="Logout"),
]

urlpatterns += [
     path('categorias/', lista_categorias, name="ListaCategorias"),
    path('temas/<int:categoria_id>/', lista_temas, name="ListaTemas"),
    path('vertema/<int:tema_id>/', ver_tema, name="VerTema"),
]
