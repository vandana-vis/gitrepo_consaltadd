from django.db import models


# Create your models here.


class Person(models.Model):
    Name = models.CharField(max_length=30)
    Contact = models.CharField(max_length=12)
    Address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Name
