import warnings

from django.core.exceptions import RemovedInDjango19Warning

warnings.warn(
    "The django.contrib.gis.db.backends.util module has been renamed. "
    "Use django.contrib.gis.db.backends.utils instead.", RemovedInDjango19Warning)

from django.contrib.gis.db.backends.utils import *  # NOQA
