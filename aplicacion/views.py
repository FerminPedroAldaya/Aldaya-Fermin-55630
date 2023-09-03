from django.shortcuts import render, redirect
from .models import Curriculum, Empleos, Empleador, Avatar, Informacion
from django.urls import reverse_lazy

from .forms import EmpleadoForm, TrabajoForm, EmpleadorForm, \
                    RegistroUsuariosForm, UserEditForm, AvatarFormulario, \
                        InformacionForm, CustomLoginForm, MensajeContactoForm

from django import template

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required




register = template.Library()

def estilizar_campo(campo, clase_css):
    return campo.as_widget(attrs={'class': clase_css})

def inicio(request):
    return render(request, "aplicacion/inicio.html")

def sobreMi(request):
    return render(request, "aplicacion/sobreMi.html")

@login_required
def nombre_usuario(request):
    nombre_usuario = request.user.username
    contexto = {'nombre_usuario': nombre_usuario}
    return render(request, "inicio.html", contexto)


#___________________________  EMPLEADO ________________________________

def lista_empleados(request):
    curriculums = Curriculum.objects.all()                          

    nombre_buscado = request.GET.get('nombre')
    if nombre_buscado:
        curriculums = curriculums.filter(nombre__icontains=nombre_buscado)

    return render(request, 'aplicacion/lista_empleados.html', {'curriculums': curriculums})



def detalle_empleado(request, curriculum_id):
    curriculum = Curriculum.objects.get(pk=curriculum_id)
    return render(request, 'aplicacion/detalle_empleado.html', {'curriculum': curriculum})


@login_required
def empleadoForm(request):
    if request.method == 'POST':
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            empleado = Curriculum(
                nombre=miForm.cleaned_data['nombre'],
                apellido=miForm.cleaned_data['apellido'],
                mail=miForm.cleaned_data['mail'],
                presentacion=miForm.cleaned_data['presentacion'],
                experiencia=miForm.cleaned_data['experiencia'],
                estudios=miForm.cleaned_data['estudios'],
                user=request.user
            )
            empleado.save()
            return redirect(reverse_lazy('lista_empleados'))

    else:
        initial_data = {
            'nombre': request.user.first_name,
            'apellido' : request.user.last_name,
            'mail': request.user.email,
            
        }
        miForm = EmpleadoForm(initial=initial_data)

    return render(request, "aplicacion/empleadoForm.html", {"form": miForm})

def updateEmpleado(request, curriculum_id):
    curriculum = Curriculum.objects.get(id=curriculum_id)
    if request.method == "POST":
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            curriculum.nombre = miForm.cleaned_data['nombre']
            curriculum.apellido = miForm.cleaned_data['apellido']
            curriculum.mail = miForm.cleaned_data['mail']
            curriculum.presentacion = miForm.cleaned_data['presentacion']
            curriculum.experiencia = miForm.cleaned_data['experiencia']
            curriculum.estudios = miForm.cleaned_data['estudios']
            curriculum.user=request.user
            curriculum.save()
            return redirect(reverse_lazy('lista_empleados'))
    else:
        miForm = EmpleadoForm(initial={
            'nombre' : curriculum.nombre,
            'apellido' : curriculum.apellido,
            'mail' : curriculum.mail,
            'presentacion' : curriculum.presentacion,
            'experiencia' : curriculum.experiencia,
            'estudios' : curriculum.estudios,
        })
    return render(request, "aplicacion/empleadoForm.html", {'form': miForm})

def deleteEmpleado(request, curriculum_id):
    curriculum = Curriculum.objects.get(id=curriculum_id)
    curriculum.delete()
    return redirect(reverse_lazy('lista_empleados'))



#________________________________  TRABAJOS________________________________ 

def lista_empleos(request):
    trabajos = Empleos.objects.all()

    trabajo_buscado = request.GET.get('cargo')
    if trabajo_buscado:
        trabajos = trabajos.filter(cargo__icontains=trabajo_buscado)
    return render(request, "aplicacion/lista_empleos.html", {'trabajos': trabajos})

def detalle_empleo(request, trabajo_id):
    trabajo = Empleos.objects.get(pk=trabajo_id)
    return render(request, 'aplicacion/detalle_empleo.html', {'trabajo': trabajo})

@login_required
def trabajoForm(request):
    if request.method == 'POST':
        miForm = TrabajoForm(request.POST)
        if miForm.is_valid():
            trabajo = Empleos(
                cargo=miForm.cleaned_data['cargo'],
                detalles=miForm.cleaned_data['detalles'],
                ubicacion=miForm.cleaned_data['ubicacion'],
                sueldo=miForm.cleaned_data['sueldo'],
                user=request.user
            )
            trabajo.save()
            return redirect(reverse_lazy('lista_empleos'))

    else:
        miForm = TrabajoForm()

    return render(request, "aplicacion/trabajoForm.html", {"form": miForm})


def updateEmpleo(request, trabajo_id):
    trabajo = Empleos.objects.get(id=trabajo_id)
    if request.method == "POST":
        miForm = TrabajoForm(request.POST)
        if miForm.is_valid():
            trabajo.cargo = miForm.cleaned_data['cargo']
            trabajo.detalles = miForm.cleaned_data['detalles']
            trabajo.ubicacion = miForm.cleaned_data['ubicacion']
            trabajo.sueldo = miForm.cleaned_data['sueldo']
            trabajo.user=request.user
            trabajo.save()
            return redirect(reverse_lazy('lista_empleos'))
    else:
        miForm = TrabajoForm(initial={
            'cargo' : trabajo.cargo,
            'detalles' : trabajo.detalles,
            'ubicacion' : trabajo.ubicacion,
            'sueldo' : trabajo.sueldo,
        })
    return render(request, "aplicacion/trabajoForm.html", {'form': miForm})

def deleteEmpleo(request, trabajo_id):
    trabajo = Empleos.objects.get(id=trabajo_id)
    trabajo.delete()
    return redirect(reverse_lazy('lista_empleos'))

#________________________________ EMPLEADOR________________________________

def lista_empleadores(request):
    empleadores = Empleador.objects.all()

    empleador_buscado = request.GET.get('nombre')
    if empleador_buscado:
        empleadores = empleadores.filter(nombre__icontains=empleador_buscado)
    return render(request, "aplicacion/lista_empleadores.html", {'empleadores': empleadores})

def detalle_empleador(request, empleador_id):
    empleador = Empleador.objects.get(pk=empleador_id)
    return render(request, 'aplicacion/detalle_empleador.html', {'empleador': empleador})

@login_required
def empleadorForm(request):
    if request.method == 'POST':
        miForm = EmpleadorForm(request.POST)
        if miForm.is_valid():
            empleador = Empleador(
                nombre=miForm.cleaned_data['nombre'],
                apellido=miForm.cleaned_data['apellido'],
                mail=miForm.cleaned_data['mail'],
                profesion=miForm.cleaned_data['profesion'],
                edad=miForm.cleaned_data['edad'],
                nombreEmpresa=miForm.cleaned_data['nombreEmpresa'],
                presentacion=miForm.cleaned_data['presentacion'],
                user=request.user
            )
            empleador.save()
            return redirect(reverse_lazy('lista_empleadores'))

    else:
        initial_data = {
            'nombre': request.user.first_name,
            'apellido' : request.user.last_name,
            'mail': request.user.email,
            
        }
        miForm = EmpleadorForm(initial=initial_data)

    return render(request, "aplicacion/empleadorForm.html", {"form": miForm})

def updateEmpleador(request, empleador_id):
    empleador = Empleador.objects.get(id=empleador_id)
    if request.method == "POST":
        miForm = EmpleadorForm(request.POST)
        if miForm.is_valid():
            empleador.nombre = miForm.cleaned_data['nombre']
            empleador.apellido = miForm.cleaned_data['apellido']
            empleador.mail = miForm.cleaned_data['mail']
            empleador.profesion = miForm.cleaned_data['profesion']
            empleador.edad = miForm.cleaned_data['edad']
            empleador.nombreEmpresa = miForm.cleaned_data['nombreEmpresa']
            empleador.presentacion = miForm.cleaned_data['presentacion']
            empleador.user=request.user
            empleador.save()
            return redirect(reverse_lazy('lista_empleadores'))
    else:
        miForm = EmpleadorForm(initial={
            'nombre' : empleador.nombre,
            'apellido' : empleador.apellido,
            'mail' : empleador.mail,
            'profesion' : empleador.profesion,
            'edad' : empleador.edad,
            'nombreEmpresa' : empleador.nombreEmpresa,
            'presentacion' : empleador.presentacion,
        })
    return render(request, "aplicacion/empleadorForm.html", {'form': miForm})

def deleteEmpleador(request, empleador_id):
    empleador = Empleador.objects.get(id=empleador_id)
    empleador.delete()
    return redirect(reverse_lazy('lista_empleadores'))

#_______________________LOGIN/REGISTRO/EDITAR PERFIL___________________________________


def login_request(request):
    if request.method == 'POST':
        miForm = CustomLoginForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/inicio.html", {'mensaje': f'Bienvenido a TrabajoYa {usuario}'})

            else:
                return render(request, "aplicacion/login.html", {"form": miForm, 'mensaje': 'Usuario o Contraseña invalidos'}) 
        else:
            return render(request, "aplicacion/login.html", {"form": miForm, 'mensaje': 'Usuario o Contraseña invalidos'})
    
    miForm = CustomLoginForm()

    return render(request, "aplicacion/login.html", {"form": miForm})

#

def registro(request):
    if request.method == 'POST':
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/inicio.html")
    else:    
        miForm = RegistroUsuariosForm()

    return render(request, "aplicacion/registro.html", {"form": miForm})

@login_required
def editar_perfil(request):
    usuario =  request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, 'aplicacion/inicio.html')
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html",{'form': form, 'usuario': usuario.username})

@login_required
def eliminar_usuario(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  
        logout(request)  
        return redirect('inicio')

    return render(request, 'aplicacion/eliminar_usuario.html')


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen

            return render(request, 'aplicacion/inicio.html')
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html",{'form': form})


#_________________________________PERFILES___________________________________

def info(request):
    if request.user.is_authenticated:
        informacion = Informacion.objects.filter(user=request.user).first()
        return informacion
    return None


    
def perfil(request):
    trabajos = Empleos.objects.all()
    empleador = Empleador.objects.all()
    curriculums = Curriculum.objects.all()
    informacion = info(request)

    return render(request, "aplicacion/perfil.html", {'trabajos': trabajos, 'empleador': empleador,'curriculums': curriculums, 'informacion': informacion})

@login_required
def agregarInformacion(request):
    if request.method == "POST":
        form = InformacionForm(request.POST)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            infoVieja = Informacion.objects.filter(user=u)
            if len(infoVieja) > 0:
                for i in range(len(infoVieja)):
                    infoVieja[i].delete()

            info = Informacion(user=u, informacion=form.cleaned_data['informacion'])
            info.save()

            informacion = Informacion.objects.get(user=request.user.id)
            request.session['info_id'] = informacion.id 

            return render(request, 'aplicacion/inicio.html')
    else:
        form = InformacionForm()
    return render(request, "aplicacion/agregarInfo.html", {'form': form})


def lista_usuarios(request):
    usuarios = User.objects.all()

    usuario_buscado = request.GET.get('username')
    if usuario_buscado:
        usuarios = usuarios.filter(username__icontains=usuario_buscado)
    return render(request, "aplicacion/lista_usuarios.html", {'usuarios': usuarios})


def detalle_usuario(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    empleado = Curriculum.objects.all()
    trabajo = Empleos.objects.all()
    empleador = Empleador.objects.all()
    informacion = Informacion.objects.all()

    try:
        avatar = Avatar.objects.get(user=usuario).imagen.url
    except Avatar.DoesNotExist:
        avatar = "/media/avatares/default.png"

    return render(request, 'aplicacion/perfilUser.html', {'usuario': usuario,'empleado': empleado,
                                                          'trabajo': trabajo,'empleador': empleador,
                                                          'informacion': informacion, 'avatar': avatar
                                                          })
@login_required
def contactar_usuario(request, destinatario_id):
    destinatario = User.objects.get(id=destinatario_id)
    if request.method == 'POST':
        form = MensajeContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.destinatario = destinatario
            mensaje.save()
            return render(request, 'aplicacion/inicio.html')

    else:
        form = MensajeContactoForm()

    return render(request, 'aplicacion/contactarForm.html', {'form': form, 'destinatario': destinatario})







    
    
            


    
