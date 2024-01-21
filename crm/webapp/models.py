from django.db import models

# Create your models here.

class Record(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)  #if any error occur then just remeber that here instead of charfield we used the emailfield
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + "   " + self.last_name
    