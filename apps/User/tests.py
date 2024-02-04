from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from faker import Faker
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework_simplejwt.tokens import RefreshToken

from apps.User.models import User


User = get_user_model()
fake = Faker()


def auth(user=None):
    refresh = RefreshToken.for_user(user)
    return {
        'HTTP_AUTHORIZATION': f'Bearer {refresh.access_token}'
    }


class UserTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username=fake.name(),
            password=fake.password(),
       )

    def test_User_list(self):
        response = self.client.get(reverse('User-list'), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_User_create(self):
        response = self.client.post(reverse('User-list'), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_User_retrieve(self):
        User_instance = User.objects.create()
        response = self.client.get(reverse('User-detail', kwargs={'pk': User_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_User_update(self):
        User_instance = User.objects.create()
        response = self.client.put(reverse('User-detail', kwargs={'pk': User_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_User_partial_update(self):
        User_instance = User.objects.create()
        response = self.client.patch(reverse('User-detail', kwargs={'pk': User_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_User_destroy(self):
        User_instance = User.objects.create()
        response = self.client.delete(reverse('User-detail', kwargs={'pk': User_instance.id}), **auth(user=self.user))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
