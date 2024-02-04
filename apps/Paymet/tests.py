from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from faker import Faker
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework_simplejwt.tokens import RefreshToken

from apps.Paymet.models import Paymet


User = get_user_model()
fake = Faker()


def auth(user=None):
    refresh = RefreshToken.for_user(user)
    return {
        'HTTP_AUTHORIZATION': f'Bearer {refresh.access_token}'
    }


class PaymetTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username=fake.name(),
            password=fake.password(),
       )

    def test_Paymet_list(self):
        response = self.client.get(reverse('Paymet-list'), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Paymet_create(self):
        response = self.client.post(reverse('Paymet-list'), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_Paymet_retrieve(self):
        Paymet_instance = Paymet.objects.create()
        response = self.client.get(reverse('Paymet-detail', kwargs={'pk': Paymet_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Paymet_update(self):
        Paymet_instance = Paymet.objects.create()
        response = self.client.put(reverse('Paymet-detail', kwargs={'pk': Paymet_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Paymet_partial_update(self):
        Paymet_instance = Paymet.objects.create()
        response = self.client.patch(reverse('Paymet-detail', kwargs={'pk': Paymet_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Paymet_destroy(self):
        Paymet_instance = Paymet.objects.create()
        response = self.client.delete(reverse('Paymet-detail', kwargs={'pk': Paymet_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
