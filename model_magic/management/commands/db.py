from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Perform various operations based on the provided command"

    def add_arguments(self, parser):
        parser.add_argument(
            "command",
            choices=["clear", "generate_data", "stress_test"],
            help="Specify the command to execute",
        )
        parser.add_argument(
            "--app_name", help="Specify the app name for generating data"
        )
        parser.add_argument(
            "--model_name", help="Specify the model name for generating data"
        )
        parser.add_argument(
            "--number_of_records",
            type=int,
            help="Specify the number of records to generate",
        )

    def handle(self, *args, **options):
        command = options["command"]

        if command == "generate_data":
            app_name = options.get("app_name")
            model_name = options.get("model_name")
            number_of_records = options.get("number_of_records")

            if not number_of_records:
                raise CommandError(
                    "Please provide values for number_of_records"
                )

            # Generate data operation
            self.stdout.write(
                f"Generating data for app: {app_name},model: {model_name}, number of records: {number_of_records}" # noqa
            )
            # Perform generate data operation

        elif command == "stress_test":
            # Stress test operation
            self.stdout.write("Performing stress test...")
            # Perform stress test operation

        else:
            raise CommandError("Invalid command specified")

        self.stdout.write(
            self.style.SUCCESS("Command execution completed successfully")
        )
