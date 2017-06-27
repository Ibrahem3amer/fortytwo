from django.db import models

class Person(models.Model):
    first_name  = models.CharField(max_length = 100, default = 'no name')
    sur_name    = models.CharField(max_length = 100, default = 'no sur name')
    bio         = models.CharField(max_length = 500, default = 'N/A')
    birth_date  = models.CharField(max_length = 100, default = 'N/A')
    contacts    = models.CharField(max_length = 200, default = '{}')

class Request(models.Model):
    scheme      = models.CharField(max_length = 100, default = 'N/A')
    body        = models.CharField(max_length = 500, default = 'N/A')
    path        = models.CharField(max_length = 100, default = 'N/A')    
    method      = models.CharField(max_length = 100, default = 'N/A')
    date        = models.CharField(max_length = 100, default = 'N/A')