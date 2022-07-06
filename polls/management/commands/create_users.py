from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Create random users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('total', choices=range(1, 11), type=int,
                            help='Indicates the number of users to be created')

    def handle(self, *args, **options):
        fake = Faker()
        users = []
        total = options['total']
        for _ in range(total):
            users.append(User(username=fake.user_name(),
                              email=fake.email(safe=False),
                              password=make_password(fake.password())))
        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'Were created {total} users'))
