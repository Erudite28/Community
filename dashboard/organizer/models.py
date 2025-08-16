from django.db import models

class volunteerroaster(models.Model):

  #volunteer list file that can be downloaded by organizers
  
  full_name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  role = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=15)
  address = models.CharField(max_length=100)
  skills = models.CharField(max_length=100)
  joined_at = models.DateTimeField(auto_now_add=True)