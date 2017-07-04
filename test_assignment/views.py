from django.shortcuts import render, get_object_or_404, redirect
from django.core.management import call_command
from django.http import HttpResponse
from test_assignment.models import Person, Request, RequestHandler
from test_assignment.forms import EditPersonForm
import json

def homepage_visitor(request):
    """
    Accepts http request, return homepage for non-authorized user. 
    """

    # In case you want to user fixture-based data.
    person = get_object_or_404(Person, pk = 1)
    
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
        person      = Person.objects.get()
        form        = EditPersonForm(request.POST, instance = person)
        response    = {}
        if(form.is_valid()):
            form.save()
            response['status'] = 'Success!'
            return HttpResponse(json.dumps(response), content_type = "application/json")
        else:
            return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}), content_type = "application/json")
    
    return render(request, 'edit_data.html')