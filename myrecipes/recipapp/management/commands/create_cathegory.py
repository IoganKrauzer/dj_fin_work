from django.core.management import BaseCommand

from recipapp.models import Cathegory


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Create cathegory')

        cathegory_names = [
            'First_courses',
            'Second_courses',
            'Snacks',
            'Salads',
        ]
        for cathegory_name in cathegory_names:
            cathegory, created = Cathegory.objects.get_or_create(name=cathegory_name)
            self.stdout.write(f'Created cathegory {cathegory.name}')

        self.stdout.write(self.style.SUCCESS('Cathegory created'))
