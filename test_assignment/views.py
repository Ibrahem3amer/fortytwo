from django.shortcuts import render, get_object_or_404
from django.core.management import call_command
from test_assignment.models import Person

def homepage_visitor(request):
    """
    Accepts http request, return homepage for non-authorized user. 
    """
    person          = Person.objects.create(
            first_name  = 'Ibrahem',
            sur_name    = 'Amer',
            birth_date  = '17-12-1995',
            bio         = 'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            contacts    = {'email': 'test_@test.com', 'phone': '01092053058', 'fb': 'ibrahem3amer'}
        )
    person.save()

    # In case you want to user fixture-based data.
    # person = get_object_or_404(Person, pk = 1)
    
    return render(request, 'home.html', {'person': person})

def latest_requests(request):
    """
    Accepts http request, calls latest 10 requests in db, display template to user. 
    """
    # Checks for new unread requests.

    # Calls latest 10 requests in db.

    # Display template to user.