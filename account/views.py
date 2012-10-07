# Create your views here.
from django.contrib.auth.views import password_reset as django_password_reset
from .forms import PasswordResetForm as reset_form

def password_reset(request):
    import pdb
    pdb.set_trace()
    redirect_to = request.POST.get("next", None)
    rv = django_password_reset(request,
                               post_reset_redirect=redirect_to,
                               password_reset_form=reset_form)
    ##TODO: flash a message here that you've reset your password
    return rv
