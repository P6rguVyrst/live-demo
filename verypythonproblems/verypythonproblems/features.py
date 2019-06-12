from .exceptions import VeryPythonException


def trigger_exception(request):
    raise VeryPythonException("Always look on the bright side of life.")
