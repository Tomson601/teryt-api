from django.core.management.base import BaseCommand
from tools.functions import STATE_DATE, CREDENTIALS, download_catalogs, establish_connection

class Command(BaseCommand):
    help = 'Download latest catalogs [SIMC, TERC, ULIC] from GUS api'

    def add_arguments(self, parser):
        parser.add_argument('-all', '--all', type=bool, help='Pass TRUE and all catalogs will be downloaded. Default False')
        parser.add_argument('-simc', '--simc', type=bool, help='Pass TRUE and only SIMC catalog will be downloaded. Default False')
        parser.add_argument('-terc', '--terc', type=bool, help='Pass TRUE and only TERC catalog will be downloaded. Default False')
        parser.add_argument('-ulic', '--ulic', type=bool, help='Pass TRUE and only ULIC catalog will be downloaded. Default False')

    def handle(self, *args, **kwargs):
        all = kwargs['all']
        simc = kwargs['simc']
        terc = kwargs['terc']
        ulic = kwargs['ulic']

        client, is_authenticated = establish_connection(CREDENTIALS)
        download_catalogs(client, is_authenticated, all=all, simc=simc, terc=terc, ulic=ulic)
