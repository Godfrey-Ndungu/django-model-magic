import sys
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Generate data for the specified app and model'

    def add_arguments(self, parser):
        parser.add_argument('number_of_records', type=int, help='Number of records to generate')
        parser.add_argument('app_name', nargs='?', type=str, help='Name of the app')
        parser.add_argument('model_name', nargs='?', type=str, help='Name of the model')

    def handle(self, *args, **options):
        number_of_records = options['number_of_records']
        app_name = options['app_name']
        model_name = options['model_name']

        if not app_name and not model_name:
            # If only number_of_records is provided
            self.stdout.write(f'Generating {number_of_records} records')
            # Your code to generate data for all apps and models goes here

        elif app_name and not model_name:
            # If app_name and number_of_records are provided
            self.stdout.write(f'Generating {number_of_records} records for app {app_name}')
            # Your code to generate data for the specified app goes here

        elif app_name and model_name:
            # If app_name, model_name, and number_of_records are provided
            self.stdout.write(f'Generating {number_of_records} records for app {app_name} and model {model_name}')
            # Your code to generate data for the specified app and model goes here

        else:
            raise CommandError('Please provide the number of records')

