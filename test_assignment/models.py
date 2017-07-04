import json
from django.core.validators import RegexValidator
from django.db import models


class Person(models.Model):
    # Helper variables
    name_validator    = RegexValidator(r'^[a-zA-Z][a-zA-Z0-9]*([ ]?[a-zA-Z0-9]+)+$', 'Name cannot start with number, should consist of characters.')

    first_name  = models.CharField(max_length = 100, validators = [name_validator], default = 'no name')
    sur_name    = models.CharField(max_length = 100, validators = [name_validator], default = 'no sur name')
    bio         = models.CharField(max_length = 500, default = 'N/A')
    birth_date  = models.CharField(max_length = 100, default = 'N/A')
    contacts    = models.CharField(max_length = 200, default = '{}')
    photo       = models.ImageField(default = 'pic_folder/None/no-img.jpg')




class Request(models.Model):
    scheme      = models.CharField(max_length = 100, default = 'N/A')
    body        = models.CharField(max_length = 500, default = 'N/A')
    path        = models.CharField(max_length = 100, default = 'N/A')    
    method      = models.CharField(max_length = 100, default = 'N/A')
    date        = models.DateTimeField(auto_now_add=True)


class RequestHandler(object):
    """Contains fields and methods that handle proccessing Request instances"""
    unread_requests_counter = 0

    @classmethod
    def save_http_request(cls, request):
        """
        Accepts http request sent by middleware, saves it to db. Return False if smth went wrong, else True. 
        """
        if 'requests' not in request.path:
            cls.increment_unread_requests()
        http_request = Request.objects.create(
                scheme  = request.scheme,
                body    = request.body,
                path    = request.path,
                method  = request.method,
            )
        http_request.save()
        return

    @classmethod
    def get_unread_requests(cls):
        """
        Returns the latest number of requests that user hasn't seen yet.
        """
        return cls.unread_requests_counter

    @classmethod
    def increment_unread_requests(cls):
        """
        Updates the number of requests that user hasn't seen yet.
        """
        cls.unread_requests_counter += 1
        return

    @classmethod
    def zero_unread_requests(cls):
        """
        Called when user vists the requests page. Make the value of unread requests to zero.
        """
        cls.unread_requests_counter = 0        
        return
