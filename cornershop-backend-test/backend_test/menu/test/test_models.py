from backend_test.menu.models import Lunch
from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestModels:
    def is_active_field(self):
        lunch = mixer.blend("menu.Lunch", is_active=True)
        assert lunch.is_active_field == True

    def is_not_active_field(self):
        lunch = mixer.blend("menu.Lunch", is_active=False)
        assert lunch.is_active_field == False
