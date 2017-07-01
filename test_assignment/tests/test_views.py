from django.core.urlresolvers import resolve
from django.urls import reverse
from django.test import TestCase

class user_vists_homepage(TestCase):
    def test_user_find_homepage(self):
        # Setup test
        request = reverse('visitor_homepage')
        request = self.client.get(request)

        # Exercise test

        # Assert test
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'home.html')

    def test_request_view(self):
        # Setup test
        request = reverse('request_page')
        request = self.client.get(request)

        # Exercise test
        # Assert test
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'requests.html')

class user_edits_personal_info(TestCase):
    def test_user_access_edit_page(self):
        # Setup test
        request = reverse('edit_personal_data')
        request = self.client.get(request)

        # Exercise test
        # Assert test
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'edit_data.html')

    def test_user_access_by_post_request_and_redirected(self):
        # Setup test
        request = reverse('edit_personal_data')
        request = self.client.post(request)

        # Exercise test
        # Assert test
        self.assertEqual(request.status_code, 302)
