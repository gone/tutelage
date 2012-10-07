from django.core.urlresolvers import reverse

from .forms import RegistrationForm, LoginForm

def login_form(request):
    if request.user.is_authenticated() or \
            request.get_full_path() == reverse("account:auth_login"):
        return {}
    login_form = LoginForm()
    return {'login_form ': login_form}


def signup_form(request):
    if request.user.is_authenticated() or \
            request.get_full_path() == reverse("account:register"):
        return {}
    signup_form = RegistrationForm()
    return {'signup_form': signup_form}
