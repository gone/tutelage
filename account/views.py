# Create your views here.
from django.contrib.auth.views import password_reset as django_password_reset
from django.contrib.auth.views import password_change as django_password_change
from django.contrib.auth.views import login as django_login

from .forms import PasswordResetForm as reset_form
from .forms import PasswordChangeForm as change_form
from .forms import LoginForm as login_form

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='')
def password_reset(request):
    redirect_to = request.POST.get("next", None)
    rv = django_password_reset(request,
                               post_reset_redirect=redirect_to,
                               password_reset_form=reset_form)
    ##TODO: flash a message here that you've reset your password
    return rv

@login_required(redirect_field_name='')
def password_change(request):
    redirect_to = request.POST.get("next", None)
    rv = django_password_change(request,
                               post_change_redirect=redirect_to,
                               password_change_form=change_form)
    ##TODO: flash a message here that you've changed your password
    return rv

#@login_required(redirect_field_name='')
def login(request):
    next = request.POST.get("next", '')
    if 'next=' in next:
        next = next[next.rindex('next=')+5:]

    rv = django_login(request,
                      authentication_form=login_form)
    ##TODO: flash a message here that you've changed your password
    if type(rv) == HttpResponseRedirect:
        return HttpResponseRedirect(next)
    return rv
