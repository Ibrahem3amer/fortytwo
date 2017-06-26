from django.core.urlresolvers import resolve
from django.urls import reverse
from django.test import TestCase
from test_assignment.views import homepage_visitor

class user_vists_homepage(TestCase):
    def test_user_find_homepage(self):
        # Setup test
        request = reverse('visitor_homepage')
        request = self.client.get(request)

        # Exercise test

        # Assert test
        self.assertEqual(request.status_code, 200)