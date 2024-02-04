from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from faker import Faker
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework_simplejwt.tokens import RefreshToken

from apps.Auto.models import Auto


User = get_user_model()
fake = Faker()


def auth(user=None):
    refresh = RefreshToken.for_user(user)
    return {
        'HTTP_AUTHORIZATION': f'Bearer {refresh.access_token}'
    }


class AutoTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username=fake.name(),
            password=fake.password(),
       )

    def test_Auto_list(self):
        response = self.client.get(reverse('Auto-list'), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Auto_create(self):
        response = self.client.post(reverse('Auto-list'), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_Auto_retrieve(self):
        Auto_instance = Auto.objects.create()
        response = self.client.get(reverse('Auto-detail', kwargs={'pk': Auto_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Auto_update(self):
        Auto_instance = Auto.objects.create()
        response = self.client.put(reverse('Auto-detail', kwargs={'pk': Auto_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Auto_partial_update(self):
        Auto_instance = Auto.objects.create()
        response = self.client.patch(reverse('Auto-detail', kwargs={'pk': Auto_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Auto_destroy(self):
        Auto_instance = Auto.objects.create()
        response = self.client.delete(reverse('Auto-detail', kwargs={'pk': Auto_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
