import re

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.validators import email_re



from registration import signals
from .forms import RegistrationForm
from app.models import Profile

class RegistrationBackend(object):
    """
    A registration backend which implements a simple
    workflow: a user supplies a email address and password
    (the bare minimum for a useful account), and is immediately signed
    up and logged in.

    """
    def register(self, request, **kwargs):
        """
        Create and immediately log in a new user.

        """
        email, password = kwargs['email'], kwargs['password1']
        username = kwargs['first_name'].lower() + kwargs['last_name'].lower()
        username = re.sub('\W', "", username)

        otherusers = User.objects.filter(username__startswith=username).count()
        username = username + str(otherusers)

        user = User.objects.create_user(username, email, password)
        Profile.objects.create(user=user)

        # authenticate() always has to be called before login(), and
        # will return the user we just created.
        new_user = authenticate(username=email, password=password)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        ##TODO: flash a message here that you've registered successfully
        return new_user

    def activate(self, **kwargs):
        raise NotImplementedError

    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:

        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.

        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.

        """
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def get_form_class(self, request):
        return RegistrationForm

    def post_registration_redirect(self, request, user):
        """
        After registration, redirect to the user's account page.

        """
        r = request.get("next") or user.get_absolute_url()
        return (r, (), {})

    def post_activation_redirect(self, request, user):
        raise NotImplementedError



class BasicBackend(object):
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class EmailBackend(BasicBackend):
    def authenticate(self, username=None, password=None):
        #If username is an email address, then try to pull it up
        if email_re.search(username):
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None
        else:
            #We have a non-email address username we should try username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user
