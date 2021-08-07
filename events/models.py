from django.db import models
from django.db.models.fields import EmailField


class Venue(models.Model):
    name=models.CharField("Venue Name", max_length=120)
    address=models.CharField(max_length=350)
    zip_code=models.CharField('Zip Code',max_length=50)
    phone=models.CharField("Content Phone", max_length=50)
    web=models.URLField("Website Address")
    email_address=models.EmailField("Email Address")
    
    def __str__(self):
        return self.name 

class Myclubuser(models.Model):
    first_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    email=models.EmailField('User Email')

    def __str__(self):
        return self.first_name+' '+self.Last_name 

# Create your models here.
class Event(models.Model):

    name = models.CharField("Event Name", max_length=50)
    event_date = models.DateTimeField("Event Date")
    venue=models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
  #  venue = models.CharField(max_length=120)
    managers = models.CharField(max_length=60)
    descripton =models.TextField(blank=True)
    attendess=models.ManyToManyField(Myclubuser,blank=True)

    def __str__(self):
        return self.name



