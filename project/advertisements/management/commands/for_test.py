from django.core.management.base import BaseCommand
from advertisements.models import Advertisement
from django.contrib.auth.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):

        user=User.objects.create(username='Ivan', password = '123456', is_staff= False)

        Advertisement.objects.create(title="Продaм холодильник",
                                     description="Хороший холодильник",
                                     status="Open",
                                     creator=user,
                                     open=True,
                                     )

        # for adv in Advertisement.objects.all():
        #     print(adv.title)

        # for adv in Advertisement.objects.filter(created_at__month__gte=2):
        #     print(adv.created_at.day)
        pass