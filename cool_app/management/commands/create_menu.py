from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = 'Loads the initial data in to database'

    def handle(self, *args, **options):

        call_command('loaddata', 'menu', verbosity=0)
        call_command('loaddata', 'items', verbosity=0)
        