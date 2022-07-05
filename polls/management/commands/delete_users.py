from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete users with id you set'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int,
                            choices=User.objects.filter(is_superuser=False).values_list('id', flat=True),
                            help='User ID. ID`s of superusers are excluded')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']
        User.objects.filter(id__in=users_ids).delete()
