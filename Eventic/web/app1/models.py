from django.db import models


# Create your models here.

class CreateEvent(models.Model):
    event_title = models.CharField(max_length=100)
    event_head = models.EmailField()
    phone = models.IntegerField()
    date=models.DateField()
    s_time=models.TimeField()
    e_time=models.TimeField()
    event_desc = models.CharField(max_length=300)
    event_type = models.CharField(max_length=20)
    event_price = models.CharField(max_length=20)
    event_value = models.CharField(max_length=20)

    class Meta:
        db_table = "event_creation"


class Register(models.Model):
    category = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    pwd = models.CharField(max_length=50)
    phone = models.IntegerField()
    cms_id = models.CharField(max_length=6)

    class Meta:
        db_table = "registered user"

