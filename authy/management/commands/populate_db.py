# populate_db.py

import json
import requests
from django.core.management.base import BaseCommand
from authy.models import Country, State, City


class Command(BaseCommand):
    help = "Populate the database with countries, states, and cities"

    def handle(self, *args, **kwargs):
        url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/countries%2Bstates%2Bcities.json"
        response = requests.get(url)
        data = response.json()

        for country_data in data:
            country, created = Country.objects.get_or_create(
                name=country_data["name"],
                code=country_data["iso3"],
                phone_code=country_data["phone_code"],
            )
            self.stdout.write(
                self.style.SUCCESS(f'Country "{country.name}" processed.')
            )

            for state_data in country_data["states"]:
                state, created = State.objects.get_or_create(
                    name=state_data["name"],
                    state_code=state_data["state_code"],
                    country=country,
                )
                self.stdout.write(
                    self.style.SUCCESS(f'  State "{state.name}" processed.')
                )

        self.stdout.write(self.style.SUCCESS("Database populated successfully."))
