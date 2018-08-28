from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, User, Permission


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Clear database from Groups and Users
        Group.objects.all().delete()
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all the Groups and Users.'))

        # Create Groups
        admin_group = Group.objects.create(name='Admin')
        self.stdout.write(self.style.SUCCESS('Successfully created "%s" group.' % admin_group.name))
        user_group = Group.objects.create(name='User')
        self.stdout.write(self.style.SUCCESS('Successfully created "%s" group.' % user_group.name))

        # Create Users
        admin = User.objects.create_user('admin', email='admin@email.com', password='password')
        admin.groups.add(admin_group)
        self.stdout.write(self.style.SUCCESS('Successfully created "%s" user with "password" as password.' % admin))
        user = User.objects.create_user('user', email='user@email.com', password='password')
        user.groups.add(user_group)
        self.stdout.write(self.style.SUCCESS('Successfully created "%s" user with "password" as password.' % user))
