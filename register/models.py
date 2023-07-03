from django.db import models
import random
import string

# Create your models here.

def generate_id():
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=7))
    return res
class Event(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    number=models.IntegerField(unique=True,null=True   )
    aid=models.CharField(max_length=10, default=generate_id)

    def __str__(self):
        return self.name