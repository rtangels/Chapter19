import json
import os.path

from django.core import management

from django.core.management.commands import loaddata
from django.core.management import BaseCommand

from catalog.models import Product, Category




class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Удаление и загрузка информации в базу данных"""

        management.call_command('flush', verbosity=0, interactive=False)
        management.call_command('loaddata', 'data.json', verbosity=0)