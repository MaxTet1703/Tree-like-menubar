from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        # call_command("create_menu")
        print("ОЧКО")
        call_command("make_user")