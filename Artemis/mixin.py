from django.utils import timezone
import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test

"""
Verifica si el usuario no Inicio Sesión
"""
def user_login(user):
	return user.is_authenticated != True

"""
Verifica si el usuario Inicio Sesión y es Admininistrador del Sistema
"""
def user_admin(user):
    return (user.is_authenticated == True) and (user.codTipoUser.codTipoUser =='admin')

"""
Verifica si el usuario Inicio Sesión y es Técnico
"""
def user_tec(user):
    return (user.is_authenticated == True) and (user.codTipoUser.codTipoUser == 'tc')

"""
Verifica si el usuario Inicio Sesión y es Gestor de Reclamos
"""
def user_grec(user):
    return (user.is_authenticated == True) and (user.codTipoUser.codTipoUser == 'grec')

"""
Verifica si el usuario Inicio Sesión y es Gestor de PQS
"""
def user_gpqs(user):
    return (user.is_authenticated == True) and (user.codTipoUser.codTipoUser == 'gpqs')

"""
Verifica si el usuario Inicio Sesión y es Gerente
"""
def user_ger(user):
    return (user.is_authenticated == True) and (user.codTipoUser.codTipoUser == 'ger')

"""
Verifica si el usuario Inicio Sesión y es Cliente
"""
def user_cli(user):
    return (user.is_authenticated == True) and (user.codTipoUser.codTipoUser == 'cli')

"""
Verifica si el usuario Inicio Sesión y es Atención al Cliente
"""
def user_atc(user):
    return (user.is_authenticated == True) and (user.codTipoUser.codTipoUser == 'atc')

"""
Verifica si el usuario Inicio Sesión y es Cliente o Gestor PQS
"""
def gpqs_cli(user):
    return (user.is_authenticated == True) and ((user.codTipoUser.codTipoUser == 'cli') or (user.codTipoUser.codTipoUser == 'gpqs'))

"""
Verifica si el usuario Inicio Sesión y es Cliente o Gestor PQS o Atención al Cliente
"""
def gpqs_atcli(user):
    return (user.is_authenticated == True) and ((user.codTipoUser.codTipoUser == 'cli') or (user.codTipoUser.codTipoUser == 'gpqs') or (user.codTipoUser.codTipoUser == 'atc'))

"""
Mixin que verifica si el Usuario Inicio Sesion y 
si no lo hizo lo devuelve al index
"""
class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion y 
si lo hizo no puede volver al index, lo devuelve a 
la pagina de inico para los usuarios
"""
class LoginAuthenticatedMixin(object):
    @method_decorator(user_passes_test(user_login,login_url='dashboard_checker'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginAuthenticatedMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Administrador del Sistema, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedAdminMixin(object):
    @method_decorator(user_passes_test(user_admin, login_url='index'))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedAdminMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Técnico, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedTecnicoMixin(object):
    @method_decorator(user_passes_test(user_tec, login_url='index'))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedTecnicoMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Gestor de Reclamos, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedGestorReclamosMixin(object):
    @method_decorator(user_passes_test(user_grec, login_url='index'))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedGestorReclamosMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Gestor de PQS, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedGestorPQSMixin(object):
    @method_decorator(user_passes_test(user_gpqs, login_url='index'))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedGestorPQSMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Gerente, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedGerenteMixin(object):
    @method_decorator(user_passes_test(user_ger, login_url='index'))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedGerenteMixin, self).dispatch(request, *args, **kwargs)


"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Cliente, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedClienteMixin(object):
    @method_decorator(user_passes_test(user_cli, login_url='index'))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedClienteMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Cliente o Gestor PQS, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedClienteGPQSMixin(object):
    @method_decorator(user_passes_test(gpqs_cli, login_url='index'))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedClienteGPQSMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Atención al Cliente, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedAtClienteMixin(object):
    @method_decorator(user_passes_test(user_atc, login_url='index'))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedAtClienteMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Gestor PQS, Cliente o Atención al CLiente, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedGPQSAtClienteClienteMixin(object):
    @method_decorator(user_passes_test(gpqs_atcli, login_url='index'))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedGPQSAtClienteClienteMixin, self).dispatch(request, *args, **kwargs)

"""
NOTA: Para la utilizacion de los Mixins en las vistas 
basadas en clases primero entra como parametro la Mixin 
y despues la Vista Generica
"""
