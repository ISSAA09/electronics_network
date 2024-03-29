from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания суперпользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@adminov.ru",
            first_name="Admin",
            last_name="Adminov",
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role="admin",
        )

        user.set_password("Q1234567")
        user.save()
