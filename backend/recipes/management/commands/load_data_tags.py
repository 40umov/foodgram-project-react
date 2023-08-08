import json

from django.core.management.base import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    help = 'Upload data to Tags'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Start command'))

        with open('data/tags.json', encoding='utf-8',
                  ) as data_file_tags:
            tags_data = json.loads(data_file_tags.read())
            for tags in tags_data:
                Tag.objects.get_or_create(**tags)

        self.stdout.write(self.style.SUCCESS('Data is uploaded'))
