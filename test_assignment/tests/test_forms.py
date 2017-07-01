from test_assignment.models import Person, Request, RequestHandler
from test_assignment.forms import EditPersonForm
from django.test import TestCase

class EditPersonFormTest(TestCase):
    def test_initiate_basic_form(self):
        # Setup test
        new_person  = Person.objects.create(
            first_name  = 'Ibrahem',
            sur_name    = 'Amer',
            birth_date  = '17-12-1995',
            bio         = 'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            contacts    = {"email": "ibrahem3amer@hotmail.com", "Jabber": "ibrahem3amer", "Skype": "ebrahem3amer"}
        )
        form        = EditPersonForm(instance = new_person)

        # Exercise test
        form.first_name = 'Magdy'

        # Assert test
        self.assertTrue(form.is_valid())

    def test_edit_fname_with_numbers(self):
        # Setup test
        new_person  = Person.objects.create(
            first_name  = 'Ibrahem',
            sur_name    = 'Amer',
            birth_date  = '17-12-1995',
            bio         = 'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            contacts    = {"email": "ibrahem3amer@hotmail.com", "Jabber": "ibrahem3amer", "Skype": "ebrahem3amer"}
        )
        form        = EditPersonForm(instance = new_person)

        # Exercise test
        form.first_name = '123'

        # Assert test
        self.assertFalse(form.is_valid())

    def test_edit_sname_with_numbers(self):
        # Setup test
        new_person  = Person.objects.create(
            first_name  = 'Ibrahem',
            sur_name    = 'Amer',
            birth_date  = '17-12-1995',
            bio         = 'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            contacts    = {"email": "ibrahem3amer@hotmail.com", "Jabber": "ibrahem3amer", "Skype": "ebrahem3amer"}
        )
        form        = EditPersonForm(instance = new_person)

        # Exercise test
        form.sur_name = '123'

        # Assert test
        self.assertFalse(form.is_valid())

    def test_edit_birth_date_with_date_less_than_10_years_ago(self):
        # Setup test
        new_person  = Person.objects.create(
            first_name  = 'Ibrahem',
            sur_name    = 'Amer',
            birth_date  = '17-12-1995',
            bio         = 'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            contacts    = {"email": "ibrahem3amer@hotmail.com", "Jabber": "ibrahem3amer", "Skype": "ebrahem3amer"}
        )
        form        = EditPersonForm(instance = new_person)

        # Exercise test
        form.birth_date = '2010'

        # Assert test
        self.assertFalse(form.is_valid())