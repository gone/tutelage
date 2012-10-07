from .forms import RegistrationForm

def login_form(request):
    if request.user.is_authenticated():
        return


        try:
            account = Account._default_manager.get(user=request.user)
        except Account.DoesNotExist:
            account = AnonymousAccount(request)
    else:
        account = AnonymousAccount(request)
    return {
        "account": account,
        "CONTACT_EMAIL": getattr(settings, "CONTACT_EMAIL", "support@example.com")
    }
