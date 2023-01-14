import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.filter(is_superuser=True).count() == 0:
            username = os.environ.get("SUPERUSER_USERNAME")
            email = os.environ.get("SUPERUSER_EMAIL")
            password = os.environ.get("SUPERUSER_PASSWORD")
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write("The superuser was created successfully")
        else:
            self.stdout.write("The superuser already exists")
