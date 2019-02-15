from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def recipient_required(function=None, redirect_field=REDIRECT_FIELD_NAME, login_url='login'):
    decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 2,
        login_url=login_url
    )

    if function:
        return decorator(function)
    return decorator

def local_body_required(function=None, redirect_field=REDIRECT_FIELD_NAME, login_url='login'):
    decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 5,
        login_url=login_url
    )

    if function:
        return decorator(function)
    return decorator
