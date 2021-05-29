from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UUIDGenerator

# Create your tests here.


class TestUUIDEndpoint(APITestCase):
    
    def test_get_request(self):
        url = reverse('get_uuids')
        response = self.client.get(url, format='json')
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(UUIDGenerator.objects.first())
        self.assertEqual(UUIDGenerator.objects.count(),1)
