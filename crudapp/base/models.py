from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=False, null=False)
    age = models.IntegerField(max_length=3)
    gender = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.name