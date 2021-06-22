
from django.urls import path  #importamos el path para rellenar los campos
from django.conf.urls.static import static    #Default

#importamos todas las listas creadas de .views y despues las agregamos en el urlpatters
from .views import add_comment_to_post,password_reset_request,eliminarAce,eliminarBat,eliminarFil,agregarAce,agregarBat,agregarFil,modificarBat,modificarAce,modificarFil,AcercaPageView,BateriasPageView,AceitesPageView,FiltrosPageView,HomePageView,RegistroPageView,registro_usuario,changePassword

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'), #default
	path('registration/registro_success',RegistroPageView.as_view(), name = 'registro_success'),
	path('registration/registrar', registro_usuario, name='registrar'),
	path('change_password/', changePassword, name = 'change_password' ),
	path('acerca',AcercaPageView.as_view(),name = 'acerca'),
	path('baterias',BateriasPageView.as_view(),name = 'baterias'),
	path('aceites',AceitesPageView.as_view(),name = 'aceites'),
	path('filtros',FiltrosPageView.as_view(),name = 'filtros'),
	path('modificarAce/<id>/',modificarAce, name = 'modificarAce'),
	path('eliminarAce/<id>/',eliminarAce, name = 'eliminarAce'),
	path('agregarAce/',agregarAce, name = 'agregarAce'),
	path('modificarBat/<id>/',modificarBat, name = 'modificarBat'),
	path('eliminarBat/<id>/',eliminarBat, name = 'eliminarBat'),
	path('agregarBat/',agregarBat, name = 'agregarBat'),
	path('modificarFil/<id>/',modificarFil, name = 'modificarFil'),
	path('eliminarFil/<id>/',eliminarFil, name = 'eliminarFil'),
	path('agregarFil/',agregarFil, name = 'agregarFil'),
	path("password_reset", password_reset_request, name="password_reset"),
]       #nombre de plantilla    nombre de la vista      nombre dado a la ruta 