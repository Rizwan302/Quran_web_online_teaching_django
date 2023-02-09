from django.db import models

# Create your models here.

class AdmissionFrom(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=20)
    lname = models.CharField(max_length=30)
    dob = models.CharField(max_length=20)
    phone = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.fname
    
