from test_assignment.models import Person, Request
from django.test import TestCase
from django.urls import reverse

class PersonTest(TestCase):
    def test_add_new_person(self):
        # Setup test
        data        = {'f_name': 'ibrahem', 's_name': 'amer', 'bio': 'bla bla bla', 'b_date': '17-12-1995', 'contact': {'email': 'test_@test.com', 'phone': '01092053058', 'fb': 'ibrahem3amer'}}
        new_person  = Person.objects.create() 

        # Exercise test
        new_person.first_name   = data['f_name']
        new_person.sur_name     = data['s_name']
        new_person.bio          = data['bio']
        new_person.birth_date   = data['b_date']
        new_person.contacts     = data['contact']
        new_person.save()
        db_result               = Person.objects.first()

        # Assert test
        self.assertEqual(data['f_name'], db_result.first_name)
        self.assertEqual(db_result, new_person)


class RequestTest(TestCase):
    def test_add_new_request_through_view(self):
        # Setup test
        self.client.get(reverse('visitor_homepage'))

        # Exercise test
        requests_in_db = Request.objects.all().count()

        # Assert test
        self.assertTrue(requests_in_db > 0)