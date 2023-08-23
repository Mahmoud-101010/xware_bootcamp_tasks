from django.db import models

class Visitor(models.Model):
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    visit_date=models.DateField(auto_now_add=True)
    
class Book(models.Model):
 fields=models.CharField(max_length=20)
 title=models.CharField(max_length=20)
 author=models.CharField(max_length=20)    