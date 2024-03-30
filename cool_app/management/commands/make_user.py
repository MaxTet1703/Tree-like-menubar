import json
from pathlib import Path

from django.contrib.auth.models import User
from django.core.management import BaseCommand





class Command(BaseCommand):

    @property
    def get_data(self):
        with open(Path().cwd() / "cool_app/fixtures/user.json", mode='r', encoding="utf-8") as file:
            data = json.loads(file.read())
            return {
                    "username": data["username"],
                    "email": data["email"],
                    "first_name": data["first_name"],
                    "last_name": data["last_name"]
                }, data["password"]
        

    def handle(self, *args, **options):
        data, password = self.get_data
        user, created = User.objects.get_or_create(data)
        if created:
            user.is_superuser = True
            user.is_active = True
            user.is_staff = True
            user.set_password(password)
            user.save()