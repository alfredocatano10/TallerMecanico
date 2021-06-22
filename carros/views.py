#Importamos los modelos y formularios de nuestra pagina, ademas de librerias para uso de operaciones
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import aceites, filtros, baterias
from .forms import AceForm, BatForm, FilForm , CustomUserForm , CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q  
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

#---------------------------------------------------------------

class HomePageView(ListView):
	model = aceites                    #nombre del modelo
	template_name = 'home.html'        #nombre de la plantilla
	context_object_name = 'docs_list'  #nombre del arreglo de los modelos

class FiltrosPageView(ListView):
	model = filtros
	template_name = 'filtros.html'
	context_object_name = 'docs_list'

class AceitesPageView(ListView):
	model = aceites
	template_name = 'aceites.html'
	context_object_name = 'docs_list'

class BateriasPageView(ListView):
	model = baterias
	template_name = 'baterias.html'
	context_object_name = 'docs_list'

class AcercaPageView(ListView):
	model = aceites
	template_name = 'acercade.html'
	context_object_name = 'docs_list'

#---------------------------------------------------------------

class RegistrarPageView (CreateView):
	model = User
	template_name = 'registration/registrar.html'
	form_class =  UserCreationForm
	success_url = reverse_lazy('registro_success')

class RegistroPageView(ListView):
	model = aceites
	template_name = 'registration/registro_success.html'

class ResetPageView (CreateView):
	model = User
	form_class =  UserCreationForm
	template_name = 'registration/reset.html'
	success_url = reverse_lazy('home')

def registro_usuario (request):
	data = {
		'form': CustomUserForm()
	}

	if request.method == 'POST':
		formulario = CustomUserForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='registro_success')
		else:
			data['form'] = formulario
			
	return render(request, 'registration/registrar.html', data)	

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})


#---------------------------------------------------------------

@permission_required('carros.add_baterias')
def agregarBat (request):
	
	if request.method == "GET":
		form = BatForm()
	else:
		form = BatForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('baterias')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'agregarBat.html', {"form": form})


@permission_required('carros.change_baterias')
def modificarBat (request, id):

	Bat = get_object_or_404(baterias, id=id)

	data = {
		'form': BatForm(instance=Bat)
	}

	if request.method == "GET":
		form = BatForm()
	else:
		form = BatForm(request.POST,request.FILES, instance=Bat)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('baterias')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'modificar.html', data)


@permission_required('carros.delete_baterias')
def eliminarBat (request, id):
	Bat = get_object_or_404(baterias, id=id)
	Bat.delete()

	return redirect(to = "baterias")




@permission_required('carros.add_aceites')
def agregarAce (request):

	if request.method == "GET":
		form = AceForm()
	else:
		form = AceForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('aceites')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'agregarAce.html', {"form": form})


@permission_required('carros.change_aceites')
def modificarAce (request, id):

	Ace = get_object_or_404(aceites, id=id)

	data = {
		'form': AceForm(instance=Ace)
	}

	if request.method == "GET":
		form = AceForm()
	else:
		form = AceForm(request.POST,request.FILES, instance=Ace)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('aceites')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'modificar.html', data)


@permission_required('carros.delete_aceites')
def eliminarAce (request, id):
	Ace = get_object_or_404(aceites, id=id)
	Ace.delete()

	return redirect(to = "aceites")




@permission_required('carros.add_filtros')
def agregarFil (request):

	if request.method == "GET":
		form = FilForm()
	else:
		form = FilForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('filtros')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'agregarFil.html', {"form": form})


@permission_required('carros.change_filtros')
def modificarFil (request, id):

	Fil = get_object_or_404(filtros, id=id)

	data = {
		'form': FilForm(instance=Fil)
	}

	if request.method == "GET":
		form = FilForm()
	else:
		form = FilForm(request.POST,request.FILES, instance=Fil)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('filtros')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'modificar.html', data)


@permission_required('carros.delete_filtros')
def eliminarFil (request, id):
	Fil = get_object_or_404(filtros, id=id)
	Fil.delete()

	return redirect(to = "filtros")

#---------------------------------------------------------------

def add_comment_to_post(request, pk):
    post = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})