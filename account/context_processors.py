from django.core.urlresolvers import reverse

from .forms import RegistrationForm, LoginForm, PasswordResetForm


def forms(request):
    forms = {}
    if request.user.is_authenticated():
        return forms
    if not request.get_full_path() == reverse("account:auth_login"):
        forms['login_form'] = LoginForm()
    if not request.get_full_path() == reverse("account:register"):
        forms['signup_form'] = RegistrationForm()
    if not request.get_full_path() == reverse("password_reset"):
        forms['fpassword_form'] = PasswordResetForm()
    return forms
