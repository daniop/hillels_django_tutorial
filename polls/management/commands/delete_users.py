from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Delete users with id you set'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int,
                            help='User ID.')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']
        superusers = User.objects.filter(is_superuser=True).values_list('id', flat=True)
        if set(superusers).intersection(set(users_ids)):
            raise CommandError('It is not allowed to delete superuser')
        deleted = User.objects.filter(id__in=users_ids).delete()
        self.stdout.write(self.style.SUCCESS(f'Were deleted { deleted[0] } objects'))
