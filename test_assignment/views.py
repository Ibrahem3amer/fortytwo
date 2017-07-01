from django.shortcuts import render, get_object_or_404, redirect
from django.core.management import call_command
from django.http import HttpResponse
from test_assignment.models import Person, Request, RequestHandler

def homepage_visitor(request):
    """
    Accepts http request, return homepage for non-authorized user. 
    """
    person          = Person.objects.create(
            first_name  = 'Ibrahem',
            sur_name    = 'Amer',
            birth_date  = '17-12-1995',
            bio         = 'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            contacts    = {"email": "ibrahem3amer@hotmail.com", "Jabber": "ibrahem3amer", "Skype": "ebrahem3amer"}
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
    unread_requests = RequestHandler.get_unread_requests()

    # Calls latest 10 requests in db.
    latest_ten_reqeusts = Request.objects.order_by('-date')[:10]
    RequestHandler.zero_unread_requests()

    # Display template to user.
    return render(request, 'requests.html', {'n': unread_requests, 'requests': latest_ten_reqeusts})

def edit_info(request):
    """
    Accepts GET request and display fillable form to user. Redirect user to homepage if POST.
    """
    if request.method == 'POST':
        return redirect('visitor_homepage')
    return HttpResponse()