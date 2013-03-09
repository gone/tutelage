"""
URLconf for registration and activation, cloned django-registration's
one-step backend.

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.
"""


from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from registration.views import activate, register
from .views import *
from .forms import LoginForm


urlpatterns = patterns('',
                       url(r'^login/?$',login, name="login"),
                       url(r'^logout/?$','django.contrib.auth.views.logout', name="logout"),
                       )


## Allows decorators to be embedded into urls, login_required being used here
## http://stackoverflow.com/questions/2307926/is-it-possible-to-decorate-include-in-django-urls-with-login-required
## http://djangosnippets.org/snippets/2607/                       

def required(wrapping_functions,patterns_rslt):
    '''
    Used to require 1..n decorators in any view returned by a url tree

    Usage:
      urlpatterns = required(func,patterns(...))
      urlpatterns = required((func,func,func),patterns(...))

    Note:
      Use functools.partial to pass keyword params to the required 
      decorators. If you need to pass args you will have to write a 
      wrapper function.

    Example:
      from functools import partial

      urlpatterns = required(
          partial(login_required,login_url='/accounts/login/'),
          patterns(...)
      )
    '''
    if not hasattr(wrapping_functions,'__iter__'): 
        wrapping_functions = (wrapping_functions,)

    return [
        _wrap_instance__resolve(wrapping_functions,instance)
        for instance in patterns_rslt
    ]

def _wrap_instance__resolve(wrapping_functions,instance):
    if not hasattr(instance,'resolve'): return instance
    resolve = getattr(instance,'resolve')

    def _wrap_func_in_returned_resolver_match(*args,**kwargs):
        rslt = resolve(*args,**kwargs)

        if not hasattr(rslt,'func'):return rslt
        f = getattr(rslt,'func')

        for _f in reversed(wrapping_functions):
            # @decorate the function from inner to outter
            f = _f(f)

        setattr(rslt,'func',f)

        return rslt

    setattr(instance,'resolve',_wrap_func_in_returned_resolver_match)

    return instance
    
urlpatterns += required(
    login_required,
    patterns('',
                      url(r'^register/$',
                           register,
                           {'backend': 'account.backends.RegistrationBackend'},
                           name='register'),
                      url(r'^register/closed/$',
                           direct_to_template,
                           {'template': 'registration/registration_closed.html'},
                           name='registration_disallowed'),
                       url(r'^password_reset/$', password_reset, name="password_reset"),
                       url(r'^password_change/$', password_change, name="password_change"),                       
                       (r'', include('registration.auth_urls')),
    )
)