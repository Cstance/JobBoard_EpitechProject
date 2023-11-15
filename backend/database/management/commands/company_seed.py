import requests
import string, random
import os
from dotenv import load_dotenv

from django.core.management.base import BaseCommand
from database.models import Companies;
class Command(BaseCommand):
    help = "Fills the database with dummy data"
    api_base_address = "https://randommer.io/api/"
    load_dotenv()

    headers = {
        "x-api-key": os.getenv("API_KEY")
    }

    def add_arguments(self, parser):
        parser.add_argument("input_size", type=int)

    def handle(self, *args, **options):
        try:
            names = requests.get(self.api_base_address + f"Name?nameType=surname&quantity={options['input_size']}", headers=self.headers)
            description = requests.get(self.api_base_address + f"text/loremipsum?loremtype=normal&type=words&number=40", headers=self.headers)
            addresses = requests.get(self.api_base_address + f"Misc/Random-Address?culture=fr&number={options['input_size']}", headers=self.headers)
            if names.status_code == 200 and description.status_code == 200 and addresses.status_code == 200:
                json_names = names.json()
                json_description = description.json()
                json_addresses = addresses.json()
                for i in range(options["input_size"]):
                    new_company = Companies(name=json_names[i], description=json_description, location= json_addresses[i], sector="Tech")
                    new_company.save()
            else:
                print("Not all api requests were successful")
        except Exception as e:
             print("An exception occurred:", e)

        self.stdout.write(
            self.style.SUCCESS('Successfully filled company table')
        )

