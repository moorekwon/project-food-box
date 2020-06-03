import unittest

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings, Client
from django.urls import reverse

image_1 = b'https://images.unsplash.com/photo-1565043534447-a83eeb658a05?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1043&q=80'


@override_settings(STATIC_ROOT='app/main/test/')
class ImageTest(TestCase):
    def test_add_image(self):
        client = Client()
        image = SimpleUploadedFile('image_1.jpg', image_1, content_type='image/jpg')
        res = client.post(reverse('main:fridge'), {'image': image, 'name': 'image_1'})
        self.assertEqual(res.status_code, 200)


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        res = self.client.get('/main/fridge/')
        self.assertEqual(res.status_code, 200)
