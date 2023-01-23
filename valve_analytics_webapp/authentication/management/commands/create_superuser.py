import os

from django.contrib.auth.management.commands import createsuperuser


class Command(createsuperuser.Command):
    help = "Create a superuser, and allow password to be provided"

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        if username and self.UserModel._default_manager.db_manager().filter(username=username).exists():
            self.stdout.write("The superuser with provided username already exists.")
            return

        super(Command, self).handle(*args, **options)
