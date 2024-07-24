from django.core.management.base import BaseCommand, CommandError
from core.models import Bank
from authy.fixtures.banks import banks as banks_data


class Command(BaseCommand):
    help = "Loads Nigerian Banks"

    def handle(self, *args, **options):
        for _, data in enumerate(banks_data):
            Bank.objects.get_or_create(name=data.get("name"), code=data.get("code"))

        self.stdout.write(
            self.style.SUCCESS("Successfully Loaded all banks to the DB ")
        )
