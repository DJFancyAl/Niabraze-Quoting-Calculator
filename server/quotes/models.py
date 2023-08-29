from django.db import models

# Create your models here.
class Quote(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length=50, blank=True, null=True)
    contact_name = models.CharField(max_length=50)
    brazed = models.BooleanField(default=False)