from django.core.management.base import BaseCommand, CommandError
from CustomCommand.settings import BASE_DIR
import json
from core.models import People

class Command(BaseCommand):
    help = "Command to read and save data from json"

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **options):
            
            file_name = options.get("file_name", None)

            try:
                if file_name:
                    with open(f"{BASE_DIR}/{file_name}") as json_file:
                        data = json.load(json_file)
                        
                        for people in data:
                            People.objects.create(**people)
                        
                        print(f"Operação realizada com sucesso.")
                        
            except Exception as e:
                raise CommandError(e)