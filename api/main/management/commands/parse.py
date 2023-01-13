from django.core.management.base import BaseCommand
from tools.functions import parse_TERC, parse_SIMC, parse_ULIC, check_file_length

class Command(BaseCommand):
    help = 'Parse catalogs located under /api/main/catalogs/'

    def add_arguments(self, parser):
        parser.add_argument('-simc', '--simc', type=bool, help='Pass TRUE and only SIMC catalog will be parsed. Default False', default=False)
        parser.add_argument('-terc', '--terc', type=bool, help='Pass TRUE and only TERC catalog will be parsed. Default False', default=False)
        parser.add_argument('-ulic', '--ulic', type=bool, help='Pass TRUE and only ULIC catalog will be parsed. Default False', default=False)

    def handle(self, *args, **kwargs):
        simc = kwargs['simc']
        terc = kwargs['terc']
        ulic = kwargs['ulic']
        
        if simc:
            file_size = check_file_length("SIMC.zip")
            user_input = input(f"File size is: {file_size} objects. Continue? [y/n] ")
            if user_input == "y":
                parse_SIMC("SIMC.zip")
            else:
                print("Aborting")
        if terc:
            file_size = check_file_length("TERC.zip")
            user_input = input(f"File size is: {file_size} objects. Continue? [y/n] ")
            if user_input == "y":
                parse_TERC("TERC.zip")
            else:
                print("Aborting")
        if ulic:
            file_size = check_file_length("ULIC.zip")
            user_input = input(f"File size is: {file_size} objects. Continue? [y/n] ")
            if user_input == "y":
                parse_ULIC("ULIC.zip")
            else:
                print("Aborting")
        else:
            print("Clean exit")
