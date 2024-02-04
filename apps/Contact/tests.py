from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from faker import Faker
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework_simplejwt.tokens import RefreshToken

from apps.Contact.models import Contact


User = get_user_model()
fake = Faker()


def auth(user=None):
    refresh = RefreshToken.for_user(user)
    return {
        'HTTP_AUTHORIZATION': f'Bearer {refresh.access_token}'
    }


class ContactTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username=fake.name(),
            password=fake.password(),
       )

    def test_Contact_list(self):
        response = self.client.get(reverse('Contact-list'), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Contact_create(self):
        response = self.client.post(reverse('Contact-list'), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_Contact_retrieve(self):
        Contact_instance = Contact.objects.create()
        response = self.client.get(reverse('Contact-detail', kwargs={'pk': Contact_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Contact_update(self):
        Contact_instance = Contact.objects.create()
        response = self.client.put(reverse('Contact-detail', kwargs={'pk': Contact_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Contact_partial_update(self):
        Contact_instance = Contact.objects.create()
        response = self.client.patch(reverse('Contact-detail', kwargs={'pk': Contact_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_Contact_destroy(self):
        Contact_instance = Contact.objects.create()
        response = self.client.delete(reverse('Contact-detail', kwargs={'pk': Contact_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_Contact_destroy(self):
        Contact_instance = Contact.objects.create()
        response = self.client.delete(reverse('Contact-detail', kwargs={'pk': Contact_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
