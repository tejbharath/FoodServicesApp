import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mfscrm.settings')
django.setup()

from crm.models import Customer as DjangoCustomer
from crm.models import Service as DjangoService
from crm.models import Product as DjangoProduct


def get_django_db():
    """Dependency to ensure Django DB connection"""
    return True
