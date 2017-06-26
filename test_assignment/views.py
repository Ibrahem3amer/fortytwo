from django.shortcuts import render
from django.core.management import call_command

def homepage_visitor(request):
    """
    Accepts http request, return homepage for non-authorized user. 
    """
    hard_coded_data = call_command('loaddata', 'data.json', app_label='test_assignment')
    return render(request, 'home.html')
