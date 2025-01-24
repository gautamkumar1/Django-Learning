from django.db import models
from django.utils import timezone
# Create your models here.
class testModel(models.Model):
    CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
  ]
    name = models.CharField(max_length=100)
    imageField = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)


def __str__(self):
    return self.name