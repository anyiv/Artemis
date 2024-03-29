from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.http import HttpResponseRedirect
from apps.usuario.models import User
from apps.resp_predefinida.models import RespuestaPredefinida
from apps.datos_externos.models import Cliente, Contrato, DetalleContrato
from apps.reclamo.models import Reclamo, HistoricoReclamo, Configuracion, Categoria
from apps.pqs.models import PQS, HistoricoPQS
from apps.usuario.forms import CrearUsuario
from django.views.generic import UpdateView, CreateView, FormView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from Artemis.mixin import LoginAuthenticatedMixin, LoginRequiredMixin
from .forms import Cambiarcontrasena
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib.auth.forms import PasswordChangeForm

# Vista que valida que un cliente esté registrado en el sistema para que un usuario
# atención al cliente pueda crear un PQRS para él.


def validar_cliente(request):
    identidad = request.POST.get('identificacion', None)

    ce = Cliente.objects.filter(identificacion=identidad, estatus='A').exists()
    cliente = usuario = None

    if ce:
        cliente = Cliente.objects.get(identificacion=identidad)

    ue = User.objects.filter(idCliente=identidad).exists()

    if ue:
        usuario = User.objects.get(idCliente=identidad)

    if usuario and cliente:
        detalle_contrato = []

        try:
            contrato = Contrato.objects.get(codCliente=cliente)
            detcon = DetalleContrato.objects.filter(nroContrato=contrato)
            for d in detcon:
                detalle_contrato.append((
                    d.codDetContrato,
                    d.codServicio.nombre
                ))
        except:
            pass

        data = {
            'cliente_existe': ce,
            'usuario_existe': ue,
            'nombre_usuario': usuario.nombreUsuario,
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'direccion': cliente.direccion,
            'servicios': detalle_contrato
        }
    else:
        data = {
            'cliente_existe': ce,
            'usuario_existe': ue
        }
    return JsonResponse(data)
# asigna reclamos a un tecnico


def asignar_tecnico(request):
    cod_reclamo = request.POST.get('cod_reclamo', None)
    id_tecnico = request.POST.get('id_tecnico', None)
    reclamo = Reclamo.objects.get(codReclamo=cod_reclamo)
    gestor = reclamo.responsableReclamo.all()[0]
    tecnico = User.objects.get(nombreUsuario=id_tecnico)
    if reclamo.responsableReclamo.all().count() != 1:
        data = {
            'respuesta': 'El reclamo ya tiene un técnico asignado.',
            'icono': 'error',
        }
    else:
        reclamo.responsableReclamo.add(tecnico)
        reclamo.save()
        hr = HistoricoReclamo()
        hr.detalle = "Se le ha asignado un técnico al reclamo."
        hr.reclamo = reclamo
        hr.usuarioEncargado = gestor
        hr.save()
        hr.notificar("se asignó un técnico")
        print(tecnico.idEmpleado.nombre)
        data = {
            'respuesta': 'Técnico asignado correctamente.',
            'icono': 'success',
            'tecnico': tecnico.idEmpleado.nombre + ' ' + tecnico.idEmpleado.apellido
        }
    return JsonResponse(data)

# obtiene la respuesta del texarea


def obtener_respuesta(request):
    codrp = request.POST.get('cod', None)
    rp = RespuestaPredefinida.objects.get(codRespuestaP=codrp)
    data = {
        'descripcion': rp.descripcion
    }
    return JsonResponse(data)

# envia la respuesta en los reclamos


def enviar_rp(request):
    try:
        respp = request.POST.get('resp', None)
        codrp = request.POST.get('codresp', None)
        codrec = request.POST.get('codrec', None)
        rec = Reclamo.objects.get(codReclamo=codrec)
        gestor = rec.responsableReclamo.all()[0]
        if rec.estatus != 'F':
            rec.estatus = 'R'
            rec.save()
        cli = rec.nombreUsuario
        cli.enviarCorreo("Nueva respuesta recibida", "Tu reclamo "+codrec +
                         " ha recibido una nueva respuesta.", "Texto de la respuesta: "+respp)
        hr = HistoricoReclamo()
        hr.reclamo = rec
        hr.detalle = "Se ha enviado una respuesta."
        hr.usuarioEncargado = gestor
        hr.save()
        hr.notificar("recibió una respuesta")
        if codrp != '-':
            rp = RespuestaPredefinida.objects.get(codRespuestaP=codrp)
            rp.contUso += 1
            rp.save()
        data = {
            'texto': 'Respuesta enviada con éxito.',
            'icono': 'success',
        }
    except:
        data = {
            'texto': 'Hubo un error en el envío.',
            'icono': 'error',
        }
    return JsonResponse(data)

# obtiene la respuesta del texarea


def obt_rp_pqs(request):
    codrp = request.POST.get('cod', None)
    rp = RespuestaPredefinida.objects.get(codRespuestaP=codrp)
    data = {
        'descripcion': rp.descripcion
    }
    return JsonResponse(data)

# envia la respuesta de las pqs


def enviar_rp_pqs(request):
    try:
        respp = request.POST.get('resp', None)
        codrp = request.POST.get('codresp', None)
        codpqs = request.POST.get('codpqs', None)
        pqs = PQS.objects.get(codPQS=codpqs)
        if pqs.estatus == 'P':
            pqs.estatus = 'A'
            pqs.save()
        hst = HistoricoPQS()
        hst.detalle = "Se ha enviado una respuesta."
        hst.pqs = pqs
        hst.usuarioEncargado = request.user
        hst.save()
        hst.notificar("recibió una respuesta")
        cli = pqs.nombreUsuario
        cli.enviarCorreo("Nueva respuesta recibida", "Tu "+pqs.get_categoria_display() +
                         " "+codpqs+" ha recibido una nueva respuesta.", "Texto de la respuesta: "+respp)
        if codrp != '-':
            rp = RespuestaPredefinida.objects.get(codRespuestaP=codrp)
            rp.contUso += 1
            rp.save()
        data = {
            'texto': 'Respuesta enviada con éxito.',
            'icono': 'success',
        }
    except:
        data = {
            'texto': 'Hubo un error en el envío.',
            'icono': 'error',
        }
    return JsonResponse(data)

# finaliza pqs


def finalizarpqs(request):
    try:
        codpqs = request.POST.get('codpqs', None)
        pqs = PQS.objects.get(codPQS=codpqs)
        pqs.estatus = 'A'
        pqs.fechaFinalizado = datetime.now()
        hst = HistoricoPQS()
        hst.detalle = "La " + pqs.get_categoria_display() + " ha sido atendida."
        hst.pqs = pqs
        hst.usuarioEncargado = request.user
        hst.save()
        hst.notificar("ha sido finalizada")
        pqs.save()
        data = {
            'texto': 'PQS finalizada con éxito.',
            'icono': 'success',
        }
    except:
        data = {
            'texto': 'Hubo un error en el envío.',
            'icono': 'error',
        }
    return JsonResponse(data)

# añade comentarios en el consultar reclamo


def anadir_comentario(request):
    try:
        codrec = request.POST.get('cod_reclamo', None)
        comentario = request.POST.get('comentario', None)
        rec = Reclamo.objects.get(codReclamo=codrec)
        hst = HistoricoReclamo()
        hst.tipo = 'C'
        hst.detalle = comentario
        hst.usuarioEncargado = request.user
        hst.reclamo = rec
        hst.save()
        data = {
            'texto': 'Comentario guardado con éxito.',
            'icono': 'success',
        }
    except:
        data = {
            'texto': 'Hubo un error guardando el comentario.',
            'icono': 'error',
        }
    return JsonResponse(data)


def guardarminymax(request):
    try:
        valormin = request.POST.get('valormin', None)
        valormax = request.POST.get('valormax', None)
        min = Configuracion.objects.get(id=1)
        max = Configuracion.objects.get(id=2)
        min.valor = valormin
        max.valor = valormax
        min.save()
        max.save()
        data = {
            'texto': 'Cambios guardados con éxito.',
            'icono': 'success',
        }
    except:
        data = {
            'texto': 'Error interno del servidor.',
            'icono': 'error',
        }
    return JsonResponse(data)


def reportefallas(request):
    try:
        fecha_i = datetime.strptime(request.POST.get(
            'fechai', None), '%Y-%m-%d') - timedelta(days=1)
        fecha_f = datetime.strptime(request.POST.get(
            'fechaf', None), '%Y-%m-%d') + timedelta(days=1)
        datos_reporte = list()
        reclamos_totales = Reclamo.objects.filter(
            fechaRegistro__range=(fecha_i, fecha_f)).count()
        for categoria in Categoria.objects.filter(estatus='A'):
            conteo = Reclamo.objects.filter(
                codCategoria=categoria, fechaRegistro__range=(fecha_i, fecha_f)).count()
            if reclamos_totales == 0:
                return JsonResponse({
                    'resultado': 'No hay datos para mostrar.'
                })
            else:
                porcentaje = round(conteo/reclamos_totales*100, 2)
            datos_reporte.append({
                'label': categoria.nombre,
                'value': porcentaje,
                'value_int': round(porcentaje, 0),
                'conteo': conteo,
            })
    except:
        return JsonResponse({
            'resultado': 'Error desconocido del servidor.'
        })
    return JsonResponse(datos_reporte, safe=False)


def reportesatisfaccion(request):
    fecha_i = datetime.strptime(request.POST.get(
        'fechai', None), '%Y-%m-%d') - timedelta(days=1)
    fecha_f = datetime.strptime(request.POST.get(
        'fechaf', None), '%Y-%m-%d') + timedelta(days=1)
    datos_reporte = list()
    reclamos_estudio = Reclamo.objects.filter(
        fechaFinalizada__range=(fecha_i, fecha_f), estatus='F')
    reclamos_totales = reclamos_estudio.count()
    for valoracion in range(0, 6):
        conteo = reclamos_estudio.filter(valoracion=valoracion).count()
        if reclamos_totales == 0:
            return JsonResponse({
                'resultado': 'No hay datos para mostrar.'
            })
        else:
            porcentaje = round(conteo/reclamos_totales*100, 2)
        datos_reporte.append({
            'label': str(valoracion) + ' estrellas',
            'value': porcentaje,
            'value_int': round(porcentaje, 0),
            'conteo': conteo,
        })
    return JsonResponse(datos_reporte, safe=False)


class index(LoginAuthenticatedMixin, SuccessMessageMixin, LoginView):
    template_name = 'index/index.html'

    def form_valid(self, form):
        if form.get_user().codTipoUser.codTipoUser == "grec":
            form.get_user().login_grec()
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())


class logout(LogoutView):
    template_name = 'index/logout.html'


class signup(LoginAuthenticatedMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = CrearUsuario
    template_name = "index/signup.html"
    success_url = reverse_lazy('index')
    success_message = "u"

class cambiar_contrasena(FormView):
    form_class = Cambiarcontrasena
    template_name = "index/cambiar_contrasena.html"
    success_url = reverse_lazy('cambiar_contrasena')
    success_message = "ec"

    def get_form_kwargs(self):
        kwargs = super(cambiar_contrasena, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        datos = form.cleaned_data
        self.request.user.set_password(datos['new_password1'])
        self.request.user.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'ec')
        return reverse_lazy('cambiar_contrasena')


class config_sistema(SuccessMessageMixin, TemplateView):
    template_name = "config_sistema.html"

    def get_context_data(self, **kwargs):
        context = super(config_sistema, self).get_context_data(**kwargs)
        context['min'] = Configuracion.objects.all()[0].valor
        context['max'] = Configuracion.objects.all()[1].valor
        return context
