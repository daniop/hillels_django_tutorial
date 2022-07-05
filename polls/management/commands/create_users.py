from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from faker import Faker


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', choices=range(1, 11), type=int,
                            help='Indicates the number of users to be created')

    def handle(self, *args, **options):
        fake = Faker()
        users = []
        for _ in range(options['total']):
            users.append(User(username=fake.user_name(),
                              email=fake.email(safe=False),
                              password=make_password(fake.password())))
        User.objects.bulk_create(users)
