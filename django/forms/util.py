import warnings

from django.core.exceptions import RemovedInDjango19Warning

warnings.warn(
    "The django.forms.util module has been renamed. "
    "Use django.forms.utils instead.", RemovedInDjango19Warning)

from django.forms.utils import *  # NOQA
