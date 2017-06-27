from django.shortcuts import render, get_object_or_404
from django.core.management import call_command
from test_assignment.models import Person

def homepage_visitor(request):
    """
    Accepts http request, return homepage for non-authorized user. 
    """
    hard_coded_data = call_command('loaddata', 'data.json', app_label='test_assignment')
    person          = get_object_or_404(Person, pk = 1)
    return render(request, 'home.html', {'person': person})
