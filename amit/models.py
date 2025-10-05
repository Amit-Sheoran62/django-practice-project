from django.db import models
from django.utils import timezone

class Variety(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='amits/')
    date_added=models.DateTimeField(default=timezone.now)
    CHOICE=[
        ('ML','MACHINE LEARNING'),
        ('PY','PYTHON'),
        ('JV','JAVA')
    ]
    type=models.CharField(max_length=2,choices=CHOICE)

    def __str__(self):
        return self.name

# Create your models here.
