from . import views
from django.urls import path
from orders.views import UserListView
from django.urls import re_path
from .views import VoluntariosListApi, SeguimientoListApi, DelegadosListApi, galeria, VoluntariosCreateAPIView, portafolio

# from ecommerce.orders.views import UserListView
urlpatterns = [
    path("listView/", UserListView.as_view(), name="listView"),
    path("", views.home),
    path('registrarVoluntarios/', views.registrarVoluntarios),
    path('edicionVoluntarios/<cedulaVoluntario>', views.edicionVoluntarios),
    path('editarVoluntarios/', views.editarVoluntarios),
    path('eliminarVoluntarios/<cedulaVoluntario>', views.eliminarVoluntarios),
    path('registrarProyectos/', views.registrarProyectos),
    path('portafolio/edicionProyectos/<idProyecto>', views.edicionProyectos),
    path('editarProyectos/', views.editarProyectos),
    path('portafolio/eliminarProyectos/<idProyecto>', views.eliminarProyectos),
     path('registrarCategorias/', views.registrarCategorias),
    path('galeria/edicionCategorias/<idCategoria>', views.edicionCategorias),
    path('editarCategorias/', views.editarCategorias),
    path('galeria/eliminarCategorias/<idCategoria>', views.eliminarCategorias),
    path('galeria/', galeria, name="galeria"),
    path('portafolio/', portafolio, name="portafolio"),
]


app_name = 'orders'

# urlpatterns = [
#     re_path(r"^getVoluntarios$", VoluntariosListApi.as_view(), name="getVoluntarios"),
#     re_path(r"^getDelegados$", DelegadosListApi.as_view(), name="getDelegados"),
#     re_path(r"^getSeguimiento$", SeguimientoListApi.as_view(), name="getSeguimiento"),
#     re_path(r"^createVoluntarios$", VoluntariosListApi.as_view(), name="createVoluntarios"),
# ]


