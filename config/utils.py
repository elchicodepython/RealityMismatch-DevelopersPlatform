from django.core.exceptions import ImproperlyConfigured
import os


def get_env_variable(var_name):
    """Get the environment variable or return excepcion."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f'Set the {var_name} environment variable.'
        raise ImproperlyConfigured(error_msg)
