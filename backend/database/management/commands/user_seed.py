import requests
import json
import string, random
import os
from dotenv import load_dotenv

from django.core.management.base import BaseCommand
from database.models import Users;
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
            names = requests.get(self.api_base_address + f"Name?nameType=fullname&quantity={options['input_size']}", headers=self.headers)
            phones = requests.get(self.api_base_address + f"phone/generate?CountryCode=fr&quantity={options['input_size']}", headers=self.headers)
            addresses = requests.get(self.api_base_address + f"Misc/Random-Address?culture=fr&number={options['input_size']}", headers=self.headers)
            if names.status_code == 200 and phones.status_code == 200 and addresses.status_code == 200:
                json_names = names.json()
                json_phones = phones.json()
                json_addresses = addresses.json()
                for i in range(options["input_size"]):
                    password = generate_random_password() 
                    first_name = json_names[i].split()[0]
                    last_name = json_names[i].split()[1]
                    print(f"Adding new user with logins : {first_name}.{last_name}@testmail.com, pwd:{password}")
                    new_user = Users(name=first_name, last_name=last_name,email=f'{first_name}.{last_name}@testmail.com', phone= json_phones[i].replace(" ", ""), location= json_addresses[i])
                    new_user.set_password(password)
                    new_user.save()
            else:
                print("Not all api requests were successful")
        except Exception as e:
             print("An exception occurred:", e)

        self.stdout.write(
            self.style.SUCCESS('Successfully filled user table')
        )

        
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password